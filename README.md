# project_env_start
vscode venv 환경 streamlit 으로 확인

my-project/

├── .gitignore          <- venv/ 를 제외하는 설정 파일

├── requirements.txt    <- streamlit, pandas 목록 파일

└── app.py              <- 작성하신 스트림릿 코드 파일

1. **프로젝트 폴더 생성**: 터미널에서 작업할 폴더를 만들고 VS Code로 엽니다.
2. **가상환경 생성**: `python -m venv venv`를 입력하여 독립된 개발 공간을 만듭니다.
3. **환경 선택**: VS Code에서 `Ctrl + Shift + P` -> `Python: Select Interpreter` 실행 -> `./venv/...` 경로 선택.
    - *Tip: 팝업창에서 "Select this environment for workspace"가 뜨면 [Yes]를 누르세요.*
4. **확장 기능**: Jupyter 확장 기능 설치 팝업이 뜨면, 이번 프로젝트는 Python 스크립트 기반이므로 [Cancel]을 눌러도 무방합니다.
5. **의존성 설치**: 루트 디렉터리에 `requirements.txt`를 생성하고 
`pip install --upgrade`를 실행
`pip install -r requirements.txt`를 실행합니다.
6. **테스트**: `streamlit run app.py`를 실행하여 브라우저에서 화면이 뜨는지 확인합니다.

<img width="1920" height="1050" alt="vscode_venv_6_streamlit_check" src="https://github.com/user-attachments/assets/aa9ffc4d-2d45-4692-95bd-45b2db0d3ced" />
