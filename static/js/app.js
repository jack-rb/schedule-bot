// Инициализация Telegram Web App
let tg = window.Telegram.WebApp;

// Инициализация приложения
document.addEventListener('DOMContentLoaded', function() {
    // Инициализируем Telegram Web App
    tg.ready();
    tg.expand();
    
    // Устанавливаем тему
    document.documentElement.style.setProperty('--tg-theme-bg-color', tg.themeParams.bg_color || '#ffffff');
    document.documentElement.style.setProperty('--tg-theme-text-color', tg.themeParams.text_color || '#000000');
    document.documentElement.style.setProperty('--tg-theme-hint-color', tg.themeParams.hint_color || '#999999');
    document.documentElement.style.setProperty('--tg-theme-button-color', tg.themeParams.button_color || '#2481cc');
    document.documentElement.style.setProperty('--tg-theme-button-text-color', tg.themeParams.button_text_color || '#ffffff');
    document.documentElement.style.setProperty('--tg-theme-secondary-bg-color', tg.themeParams.secondary_bg_color || '#f8f9fa');
    
    // Загружаем группы при старте
    loadGroups();
    
    // Обработчик изменения группы
    document.getElementById('groupSelect').addEventListener('change', function() {
        const selectedGroup = this.value;
        if (selectedGroup) {
            loadSchedule(selectedGroup);
        } else {
            hideAllStates();
            showState('empty');
        }
    });
});

// Загрузка групп
async function loadGroups() {
    try {
        showState('loading');
        
        const response = await fetch('/api/schedule');
        const data = await response.json();
        
        if (data.success && data.data) {
            // Извлекаем уникальные группы
            const groups = [...new Set(data.data.map(item => item.group.name))];
            
            const groupSelect = document.getElementById('groupSelect');
            
            // Очищаем существующие опции
            groupSelect.innerHTML = '<option value="">Выберите группу</option>';
            
            // Добавляем группы
            groups.forEach(group => {
                const option = document.createElement('option');
                option.value = group;
                option.textContent = group;
                groupSelect.appendChild(option);
            });
            
            hideAllStates();
            showState('empty');
        } else {
            throw new Error(data.error || 'Ошибка загрузки групп');
        }
    } catch (error) {
        console.error('Ошибка загрузки групп:', error);
        showError('Ошибка загрузки групп: ' + error.message);
    }
}

// Загрузка расписания
async function loadSchedule(groupName = null) {
    try {
        showState('loading');
        
        const url = groupName ? `/api/schedule/${encodeURIComponent(groupName)}` : '/api/schedule';
        const response = await fetch(url);
        const data = await response.json();
        
        if (data.success && data.data) {
            displaySchedule(data.data);
        } else {
            throw new Error(data.error || 'Ошибка загрузки расписания');
        }
    } catch (error) {
        console.error('Ошибка загрузки расписания:', error);
        showError('Ошибка загрузки расписания: ' + error.message);
    }
}

// Отображение расписания
function displaySchedule(schedules) {
    if (!schedules || schedules.length === 0) {
        showState('empty');
        return;
    }
    
    const scheduleContent = document.getElementById('scheduleContent');
    scheduleContent.innerHTML = '';
    
    // Группируем расписание по дням недели
    const scheduleByDay = {};
    
    schedules.forEach(schedule => {
        const day = schedule.day_of_week;
        if (!scheduleByDay[day]) {
            scheduleByDay[day] = [];
        }
        scheduleByDay[day].push(schedule);
    });
    
    // Сортируем дни недели
    const dayOrder = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'];
    
    dayOrder.forEach(day => {
        if (scheduleByDay[day]) {
            const daySchedule = createDaySchedule(day, scheduleByDay[day]);
            scheduleContent.appendChild(daySchedule);
        }
    });
    
    showState('schedule');
}

// Создание блока расписания на день
function createDaySchedule(dayName, lessons) {
    const dayDiv = document.createElement('div');
    dayDiv.className = 'day-schedule fade-in';
    
    const dayHeader = document.createElement('div');
    dayHeader.className = 'day-header';
    dayHeader.textContent = dayName;
    
    const lessonsDiv = document.createElement('div');
    lessonsDiv.className = 'lessons';
    
    // Сортируем уроки по номеру
    lessons.sort((a, b) => a.lesson_number - b.lesson_number);
    
    lessons.forEach(lesson => {
        const lessonDiv = createLessonElement(lesson);
        lessonsDiv.appendChild(lessonDiv);
    });
    
    dayDiv.appendChild(dayHeader);
    dayDiv.appendChild(lessonsDiv);
    
    return dayDiv;
}

// Создание элемента урока
function createLessonElement(lesson) {
    const lessonDiv = document.createElement('div');
    lessonDiv.className = 'lesson';
    
    const lessonNumber = document.createElement('div');
    lessonNumber.className = 'lesson-number';
    lessonNumber.textContent = lesson.lesson_number;
    
    const lessonContent = document.createElement('div');
    lessonContent.className = 'lesson-content';
    
    const lessonSubject = document.createElement('div');
    lessonSubject.className = 'lesson-subject';
    lessonSubject.textContent = lesson.subject;
    
    const lessonDetails = document.createElement('div');
    lessonDetails.className = 'lesson-details';
    
    // Добавляем детали урока
    const details = [];
    
    if (lesson.time_start && lesson.time_end) {
        details.push(`🕐 ${lesson.time_start}-${lesson.time_end}`);
    }
    
    if (lesson.room) {
        details.push(`🏠 ${lesson.room}`);
    }
    
    if (lesson.teacher) {
        details.push(`👨‍🏫 ${lesson.teacher}`);
    }
    
    details.forEach((detail, index) => {
        const detailSpan = document.createElement('span');
        detailSpan.className = 'lesson-detail';
        detailSpan.textContent = detail;
        lessonDetails.appendChild(detailSpan);
    });
    
    lessonContent.appendChild(lessonSubject);
    lessonContent.appendChild(lessonDetails);
    
    lessonDiv.appendChild(lessonNumber);
    lessonDiv.appendChild(lessonContent);
    
    return lessonDiv;
}

// Показать состояние
function showState(state) {
    hideAllStates();
    document.getElementById(state).classList.remove('hidden');
}

// Скрыть все состояния
function hideAllStates() {
    const states = ['loading', 'error', 'empty', 'schedule'];
    states.forEach(state => {
        document.getElementById(state).classList.add('hidden');
    });
}

// Показать ошибку
function showError(message) {
    const errorDiv = document.getElementById('error');
    const errorText = errorDiv.querySelector('p');
    errorText.textContent = message;
    showState('error');
}

// Обработка ошибок сети
window.addEventListener('online', function() {
    console.log('Соединение восстановлено');
    loadGroups();
});

window.addEventListener('offline', function() {
    console.log('Соединение потеряно');
    showError('Нет подключения к интернету');
}); 