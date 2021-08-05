# Python Code For Raspberry Pi
Lasers are functional:
    If you get errorno 121, check wiring
    Add pins connected to laser XSHUT pins to commented list
    
If using DIO sensors: 
    Copy line mentioning linit switch for all sensors

For LEDs:
    Set LightCount to the number of LEDs
    Choose message or rotate
    Change delay, to balance LED animations with sensor outputs
  
RIO coms:
    Are currently iffy, Plan is to make it USB primary with Rx/Tx pin option commented
