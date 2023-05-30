// Task list functionality
const taskInput = document.getElementById('task-input');
const taskList = document.getElementById('task-list');
let taskId = 0;

function addTask() {
    const task = taskInput.value;
    if (task) {
        const li = document.createElement('li');
        li.innerHTML = `${task}<button onclick="deleteTask(${taskId})">Delete</button>`;
        li.id = `task-${taskId}`;
        taskList.appendChild(li);
        taskInput.value = '';
        taskId++;
    }
}

function deleteTask(id) {
    const task = document.getElementById(`task-${id}`);
    task.remove();
}

// Pomodoro timer functionality
let timerInterval;
let minutes = 25;
let seconds = 0;

function startTimer() {
    timerInterval = setInterval(updateTimer, 1000);
}

function stopTimer() {
    clearInterval(timerInterval);
}

function resetTimer() {
    clearInterval(timerInterval);
    minutes = 25;
    seconds = 0;
    updateTimerDisplay();
}

function updateTimer() {
    if (minutes === 0 && seconds === 0) {
        clearInterval(timerInterval);
        alert('Timer finished!');
        return;
    }

    if (seconds === 0) {
        minutes--;
        seconds = 59;
    } else {
        seconds--;
    }

    updateTimerDisplay();
}

function updateTimerDisplay() {
    const minutesDisplay = padNumber(minutes);
    const secondsDisplay = padNumber(seconds);
    const timerDisplay = document.getElementById('timer-display');
    timerDisplay.innerHTML = `${minutesDisplay}:${secondsDisplay}`;
}

function padNumber(number) {
    if (number < 10) {
        return `0${number}`;
    }
    return number;
}
