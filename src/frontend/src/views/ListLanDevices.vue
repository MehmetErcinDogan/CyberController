<template>
    <div class="full-screen-container">
        <div class="up-container">
          
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
<style>
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
    margin-top: 7%;
  display: flex;
  align-items: center;
  margin-bottom: 20px; /* Aradaki mesafeyi azaltmak için */
  margin-left: 90%;
}

.down-container {
  display: flex;
  align-items: center;
  margin-bottom: 100px;
}




.alt-label{
  width: 100%;
    height: 1000px;
    border-radius: 5px;
    background-color: rgba(204, 31, 161, 0.245);

  margin-right: 20px;
  margin-bottom: 10px; /* Listing Devices başlığını bir miktar aşağı kaydır */
}

.a2{
  margin-top: 1%;
  margin-left: 2%;
  font-size: 18px;
  font-family: "Roboto Flex", sans-serif;



}
.btn1{
  margin-left: 20%;
  
    
    border: none;
    outline: none;
    padding: 8px 20px; /* Buton boyutunu küçültmek için padding'i azaltın */
    background: #ff5945;
    color: #fff;
    font-size: 24px; /* Font boyutunu biraz küçültün */
    cursor: pointer;
    border-radius: 15px; /* Daha yuvarlak köşeler için border-radius'u artırın */
    transition: background 0.3s ease; /* Hover efektini yumuşak hale getirin */
    height: 50px;
    font-family: "Roboto Flex", sans-serif;


}

.Lp2{
  font-size: 18px;
  color: white;
  font-family: "Roboto Flex", sans-serif;


}

</style>