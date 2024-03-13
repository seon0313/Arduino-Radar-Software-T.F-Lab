# Arduino-Radar-Software

## 개요
T.F Lab의 정기 프로젝트 Arduino Radar의 소프트웨어(뷰어) 이다.

하드웨어: https://github.com/seon0313/Arduino-Radar-Hardware

***

## 초기 설정

main.py의 10번째 Line

``` arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1) ```

위 코드에서 ```port='COM3'``을 연결할 아두이노의 포트로 설정한다.

예) 연결할 아두이노의 포트가 COM4일 경우

``` arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1) ```

개발 중인 소프트웨어이므로 추후 자동 탐색 기능을 추가할 예정이다.

***

## LICENSE

Apache-2.0 license

T.F Lab의 로고는 T.F Lab 동아리에 있음.

개발: T.F Lab 추윤선
