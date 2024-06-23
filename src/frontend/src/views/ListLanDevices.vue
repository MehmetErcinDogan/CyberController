<template>
    <div class="full-screen-container">
        <div class="up-container">
          <!-- Burda bir button var. Bu buttona basıldığında localdeki cihazların ip leri çıkarılacak. -->
          <!-- Bu adresler aşağıdaki local ıp name başlıklı kısmın altında yazılacak. -->
          
          <button class="btn1">Button</button>
        </div>
        <div class="down-container">
          <div class="alt-label">
            
            <div class="a2">
              <h1 class="Lp2">Local Ip Name</h1>
            </div>
          </div>
        </div>
    </div>


</template>
<script>

</script>
<style scoped>
.full-screen-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  font-family: "Roboto Flex", sans-serif;
  overflow-x: hidden;
}

.up-container {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  margin: 5% 5%; /* Dinamik marjin için yüzde kullanımı */
}

.down-container {
  display: flex;
  justify-content: center; /* Ortalamak için center kullanımı */
  align-items: center;
  flex-grow: 1;
  width: 100%; /* Full width */
}

.alt-label {
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  border-radius: 5px;
  background-color: rgba(204, 31, 161, 0.245);
  margin: 20px 0; /* Yatay margin kaldırıldı */
  padding: 20px;
  border-radius: 15px;
}

.a2 {
  margin-top: 1%;
  margin-left: 2%;
  font-size: 18px;
}

.btn1 {
  border: none;
  outline: none;
  padding: 8px 20px;
  background: #ff5945;
  color: #fff;
  font-size: 18px; /* Daha küçük font boyutu */
  cursor: pointer;
  border-radius: 15px;
  transition: background 0.3s ease;
  height: 40px;
  margin-top: 3%;
}

.Lp2 {
  font-size: 18px;
  color: white;
}

@media (max-width: 768px) {
  .up-container {
    margin: 5% 10%; /* Daha küçük cihazlar için marjin ayarlaması */
    justify-content: center; /* Butonu ortalamak için center kullanımı */
  }

  .btn1 {
    font-size: 16px; /* Daha küçük cihazlar için font boyutunu ayarlama */
    height: 40px;
    padding: 5px 15px;
  }

  .down-container {
    margin: 10px 0; /* Daha küçük cihazlar için marjin ayarlaması */
  }

  .alt-label {
    width: 100%; /* Full width */
    height: auto; /* Yüksekliği içeriğe göre ayarla */
  }

  .a2 {
    font-size: 16px;
  }
}


</style>