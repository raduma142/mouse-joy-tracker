// пин подключения контакта VRX
#define PIN_VRX A0
// пин подключения контакта VRY
#define PIN_VRY A1
// пин подключения кнопки
#define PIN_BUTTON 3

void setup () {
   // запуск последовательного порта
   Serial.begin (9600);
}

void loop () {
   // Выводим значение по оси X
   Serial.print(analogRead(PIN_VRX));
   Serial.print(" ");
   // Выводим значение по оси Y
   Serial.print(analogRead(PIN_VRY));
   Serial.print(" ");
   // Состояние кнопки
   Serial.println(!(digitalRead(PIN_BUTTON) == HIGH));
}