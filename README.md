# ADP_study

### ✅ 깃헙 Push/Pull 규칙

1. 무조건 __pull__ 먼저 해줍니다. pull을 해서 해당 주차의 디렉토리가 생기지 않는다면 따로 만들어주세요

```
$ git pull <remote 이름> <브랜치이름>
$ git pull AlgorithmStudy master
```

2. 파일 업로드 규칙에 맞게 push해주세요.
```
$ git add .
$ git commit -m "BOJ_1000_홍길동"
$ git push <remote 이름> master
```

3. 만일 push를 하다가 __충돌__ 이 일어났을 경우 아래의 코드를 입력해주세요
```
$ git log --oneline
```
입력 후 내가 push한 커밋 바로 전 커밋 코드를 복사해줍니다. 그리고 다음을 입력해주세요
```
$ git reset --soft [복사한 커밋 코드]
```

4. 만일 내가 올린 코드에 수정/추가 등의 추가 커밋을 push할 경우에 커밋 형식을 다음과 같이 작성해주세요. 수정을 2번째 할 경우에 `fix2`를 붙여주시면 됩니다.

```
git commit -m "BOJ_1000_홍길동_fix"
git commit -m "BOJ_1000_홍길동_add"
```

### 💕 원격 저장소 등록하기
1. 원하는 디렉토리에 clone해서 다운받습니다. 

```bash
$ git clone https://github.com/Trailblazer-Yoo/Algorithm_Study
```

2. `git remote add <원격저장소 이름> <주소>` 형식으로 작성합니다.

```bash
$ git remote add algorithmStudy https://github.com/Trailblazer-Yoo/Algorithm_Study
```

### 💕 원격 저장소 조회


`git remote -v`로 등록이 잘 됐는지 확인해봅니다.
```
$ git remote -v
algorithmStudy https://github.com/Trailblazer-Yoo/Algorithm_Study (fetch)
algorithmStudy https://github.com/Trailblazer-Yoo/Algorithm_Study (push)