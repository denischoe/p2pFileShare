이 프로그램은 두명의 유저가 데스크탑 혹은 모바일에서 크롬 브라우저(>=50)를 통해  파일을 실시간으로 공유 할 수 있는 프로그램입니다.
(두명 이상의 유저는 지원하지 않습니다. )


서버 구동 방법 on mac osx system. ( python >= 2 버전 필요)

	1. 먼 저 터미널창을 열고 signalingServer.py (서버 프로그램) 파일이 있는 곳으로 들어갑니다.
     		예) cd /FileLocation/

	2. 가상 환경에서 서버를 구동 하기 위해 virtualenv 프로그램을 다운 받아야합니다.
		예) pip install virtualenv
	3. 다음 프로그램을 실행시켜 가상 환경을 만듭니다.
		예) sudo virtualenv venv 
	4.가상 환경이 만들어졌으면 가상환경을 활성화합니다.
     		예) source venv/bin/activate
		- 종료시 deactivate 
		- 성공시 (venv)표시가 맨 왼쪽끝에 보입니다.
	5. 이후 pip 을 이용하여 필요한 모듈등을 설치 합니다.
		예) sudo pip install Flask flask-socketio
		   
	3. 모듈들이 다 설치되었으면  signalingServer.py 를 실행 시킵니다.
	       예) python signalingServer.py (optional url)
	       예)python signalingServer.py 192.168.X.X

	 ( 별도의 웹 서버를 이용 할시에는 그 서버에 맞는 python wsgi 모듈설치와 virtual host conf 변경이 필요합니다. )

앱 실행방법 ( chrome web browser 이용 바람.)

	1. 먼저 두명 혹은 한명의 유저가 앱을 엽니다.
		예) localhost:5000/  or 192.X.X.X:5000/ on the LAN.   

	2. 받고자 하는 사람은 offer 버튼을 누르면 보내고자하는 사람의 부라우저에 알람창을 뛰웁니다. 

	3. 그러면 보내는 사람은 send 버튼을 눌러 원하는 파일을 보냅니다.

	4. 전송이 끝나면 받는사람 웹 창에 알람 메세지와 함께 다운로드 링크가 생깁니다.

	5. 보내는 사람은 그 후에 계속 원하는 파일을 지속적으로 보낼 수 있지만 그전에 보냈던 파일은 무시 됩니다.

	- 보내는 사람과 받는사람을 바꾸고 싶다면 그냥 새로고침 하시면 됩니다 ^^;;

	주의 : 한글이름 파일이 되지 않을시 영문 으로만 되어있는  파일을 보내시기 바랍니다.

	

