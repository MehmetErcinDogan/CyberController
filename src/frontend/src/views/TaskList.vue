<template>
    <div class="full-screen-container">
        <div class="Task-List-Vue">
      <h2>Task List<img src="/images/icon.png"></h2>
      <div class="row">
        <input type="text" v-model="taskInput" placeholder="Yeni görev girin.">
        <button @click="addTask">Görev Ekle</button>
      </div>
      <ul class="task-list" id="list-container" @click="handleClick">
        <li v-for="(task, index) in tasks" :key="index" :class="{ checked: task.checked }">
          {{ task.title }}
          <span class="close">×</span>
        </li>
      </ul>
  
    </div>

    </div>
    
  
  
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  
  
  const taskInput = ref('');
  const tasks = ref([]);
  
  const addTask = () => {
    if (taskInput.value === '') {
      alert("Bir şey yazmalısın!");
    } else {
      tasks.value.push({ title: taskInput.value, checked: false });
      taskInput.value = '';
      saveData();
  
    }
  };
  
  const removeTask = (index) => {
    tasks.value.splice(index, 1);
    saveData();
  
  };
  
  const handleClick = (e) => {
    if (e.target.tagName === "LI") {
      const index = Array.from(e.target.parentElement.children).indexOf(e.target);
      tasks.value[index].checked = !tasks.value[index].checked;
    } else if (e.target.tagName === "SPAN") {
      const index = Array.from(e.target.parentElement.parentElement.children).indexOf(e.target.parentElement);
      removeTask(index);
    }
  };
    // Bu aşağıdaki 3 fonksiyonda değişiklikler yapmak lazım. Çünkü kaydedilen tasklar locale kaydediliyor.
  const saveData = () => {
    localStorage.setItem("tasks", JSON.stringify(tasks.value));
  };
  
  const loadData = () => {
    const storedTasks = localStorage.getItem("tasks");
    if (storedTasks) {
      tasks.value = JSON.parse(storedTasks);
    }
  };
  
  onMounted(loadData);
  
  
  </script>
  <style>
  *{
    
    
    font-family: "Roboto Flex", sans-serif;

    
  }
  .full-screen-container {
  position: relative;
  width: 100vw; /* Ekran genişliği kadar */
  height: 100vh; /* Ekran yüksekliği kadar */
  overflow-x: hidden;

}
  .Task-List-Vue{
    
    width: 540px;
    background: #fff;
    margin: 100px auto 20px;
    padding: 40px 30px 70px;
    border-radius: 10px;
    margin-left: 100px;
  
  }
  .h2{
    color: #002765;
    display: flex;
    align-items: center;
    margin-bottom: 20px;
    font-family: sans-serif;
  
  }
  .Task-List-Vue h2 img{
    width: 30px;
    margin-left: 10px;
  
  }
  .row{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #edeef0;
    border-radius: 30px;
    padding-left: 20px;
    margin-bottom: 25px;
  
  }
  input{
    flex: 1;
    border: none;
    outline: none;
    background: transparent;
    padding: 10px;
  }
  button{
    border: none;
    outline: none;
    padding: 16px 50px;
    background: #ff5945;
    color: #fff;
    font-size: 16px;
    cursor: pointer;
    border-radius: 40px;
  }
  .Task-List-Vue .task-list li {
    list-style: none;
    font-size: 17px;
    padding: 12px 8px 12px 50px;
    user-select: none;
    cursor: pointer;
    font-family: sans-serif;
    position: relative;
}

.Task-List-Vue .task-list li::before {
    content: '';
    position: absolute;
    height: 28px;
    width: 28px;
    border-radius: 50%;
    background-image: url(images/unchecked.png);
    background-size: cover;
    background-position: center;
    top: 12px;
    left: 8px;
}

.Task-List-Vue .task-list li.checked {
    color: #555;
    text-decoration: line-through;
}

.Task-List-Vue .task-list li.checked::before {
    background-image: url(images/checked.png);
}

.Task-List-Vue .task-list li span {
    position: absolute;
    right: 0;
    top: 5px;
    width: 40px;
    height: 40px;
    font-size: 22px;
    color: #555;
    line-height: 40px;
    text-align: center;
    border-radius: 50%;
}

.Task-List-Vue .task-list li span:hover {
    background: #edeef0;
}
  
  </style>