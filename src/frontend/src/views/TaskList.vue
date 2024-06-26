<template>
    <div class="full-screen-container">
        <div class="Task-List-Vue">
      <h2>Task List<img src="/images/icon.png"></h2>
      <div class="row">
        <input class="t1" type="text" v-model="taskInput" placeholder="Yeni görev girin.">
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
  
 
  let ws;

  const HandleConnection = () => {
    const ws = new WebSocket("ws://172.16.0.229:5000");
    
    ws.onopen = function() {
      ws.send("#INIT");
    };
    
    ws.onmessage = function(event) {
      if(event.data == "#ALLOW"){
        //pass
      }else if (event.data === "#DENY"){
        router.push("/login");
      } else {
        let msg = JSON.parse(event.data);
        localStorage.setItem("msg", JSON.stringify(msg));
        console.log(msg);
      }
      
    };

    ws.onerror = function(error) {
      console.log("WebSocket error: ", error);
      router.push('/');
    };

    return ws;
  };

  const sendMessage = (ws, message) => {
    if (ws.readyState === WebSocket.OPEN) {
      ws.send(message);
    } else {
      ws.addEventListener('open', () => {
        ws.send(message);
      }, { once: true });
    }
  };

  onMounted(()=>{
    try{
      ws = HandleConnection();
      sendMessage(ws,"#CHECK "+localStorage.id);
      sendMessage(ws,"#GETTASK");
      loadData();
    } catch {
      console.log("Error at onMounted");
    }
  });


  </script>
  <style scoped>
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
    font-style: italic;
  
  font-family: "Roboto Flex", sans-serif;
  
  }
  .h2{
    color: #002765;
    display: flex;
    align-items: center;
    margin-bottom: 20px;
    font-style: italic;
  
  font-family: "Roboto Flex", sans-serif;
  
  }
  .t1{
  font-style: italic;
  
  font-family: "Roboto Flex", sans-serif;
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
    font-style: italic;
    font-weight: bold;
  }
  .Task-List-Vue .task-list li {
    list-style: none;
    font-size: 17px;
    padding: 12px 8px 12px 50px;
    user-select: none;
    cursor: pointer;
    font-family: sans-serif;
    position: relative;
    font-style: italic;
  
  font-family: "Roboto Flex", sans-serif;
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