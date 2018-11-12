/*
#****************************************************************************************************************************
#   --------------------------------------------------------------------------------------------------------------------
#   @Autecla: Testing the functions of AuTecla with Circular Buffer
#   Sketch/program to testing the functions of AuTecla with circular buffer
#   --------------------------------------------------------------------------------------------------------------------
#****************************************************************************************************************************
*/

//----------------------------------------------------//

#ifdef DEBUG
#define DEBUG_PRINT(x)  Serial.print(x)
#define DEBUG_PRINTLN(x) Serial.println(x)
#define DEBUG_PRINT2(x, y) Serial.print(x, y)
#define DEBUG_PRINTLN2(x, y) Serial.println(x, y)
#else
#define DEBUG_PRINT(x)
#define DEBUG_PRINTLN(x)
#define DEBUG_PRINT2(x, y)
#define DEBUG_PRINTLN2(x, y)
#endif

//----------------------------------------------------//

int count_get = 0;
int count_store = 0;

//----------------------------------------------------//

struct id {
  char id[30];
};

struct id matriz_id[4][4];

struct bfr {
  char data_rfid[30];
  bool has_data;
};

struct bfr buffer_data[50]; //tá 50 por enquanto, colocar 80 depois

//----------------------------------------------------//

void get_data_from_rfid(){
  Serial.println("======get_data_from_rfid======");
  if(Serial.available() > 0){
    
    Serial.readBytesUntil( '\n',buffer_data[count_get].data_rfid,30);
    delay(1000);
    //OS PRINTS DE DEBUG    
    Serial.print("Buffer_data:");
    Serial.println(buffer_data[count_get].data_rfid);
    Serial.print("Count_get:");
    Serial.println(count_get);
    Serial.print("has_data:");
    Serial.println(buffer_data[count_get].data_rfid);
    
    buffer_data[count_get].has_data = 1;
    
    //OS PRINTS DE DEBUG
    Serial.print("has_dataNew:");
    Serial.println(buffer_data[count_get].data_rfid);
    
    count_get = (count_get + 1) % 50; //tá 50 por enquanto, colocar 80 depois
    
    //OS PRINTS DE DEBUG
    Serial.print("Count_getNew:");
    Serial.println(count_get);
  }
  Serial.println("Saindo do get");
}

//----------------------------------------------------//

void store_data(){
  Serial.println("======store_data======");
  int linha = 0;
  int coluna = 0;
  //char bfr_cadastro[30];
  int i = 0;
  //while (Serial.available() > 0) {
  linha = buffer_data[count_store].data_rfid[2];
  coluna = buffer_data[count_store].data_rfid[4];
  for(i = 4; i<30; i++)
  {
    matriz_id[linha][coluna].id[i-4] = buffer_data[count_store].data_rfid[i]; 
  }
  
  //OS PRINTS DE DEBUG
  Serial.print("Dado:");
  Serial.println(buffer_data[count_store].data_rfid);
  Serial.print("Matriz:");
  Serial.println(matriz_id[linha][coluna].id);
  Serial.print("Count_store:");
  Serial.println(count_store);

  count_store = (count_store + 1) % 50; //tá 50 por enquanto, colocar 80 depois
  
  //OS PRINTS DE DEBUG
  Serial.print("Count_storeNew:");
  Serial.println(count_store);
}

void setup() {
  Serial.begin(115200);
  Serial.println("Começando o SETUP");
  //put your setup code here, to run once:
  count_get = 0;
  count_store = 0;
  delay(2000);
  memset(matriz_id, 0, 480);
  memset(buffer_data, 0,1500);
  Serial.println("Terminando o SETUP");
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println("Começando o loop");
  if(Serial.available() > 0){
     char bfr[1500];
     memset(bfr,0, 1501);
     Serial.readBytesUntil( '\n',bfr,1500);
     Serial.print("BFR:");
     Serial.println(bfr);
   /* Serial.readBytesUntil( '\n',buffer_data[count_get].data_rfid,30);
    delay(1000);
    //OS PRINTS DE DEBUG    
    Serial.print("Buffer_data:");
    Serial.println(buffer_data[count_get].data_rfid);
    Serial.print("Count_get:");
    Serial.println(count_get);
    Serial.print("has_data:");
    Serial.println(buffer_data[count_get].data_rfid);
    
    buffer_data[count_get].has_data = 1;
    
    //OS PRINTS DE DEBUG
    Serial.print("has_dataNew:");
    Serial.println(buffer_data[count_get].data_rfid);
    
    count_get = (count_get + 1) % 50; //tá 50 por enquanto, colocar 80 depois
    
    //OS PRINTS DE DEBUG
    Serial.print("Count_getNew:");
    Serial.println(count_get);*/
  }
  //delay(1000);
  //store_data();
  //delay(1000);
}
