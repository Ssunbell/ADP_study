# 🔥 ADP 스터디 🔥

<img src="https://user-images.githubusercontent.com/97590480/236661481-dfd98434-87a7-4942-81f0-d9e5ec7f8031.png">

저희는 2023년 6월 or 9월 시험에서 ADP 실기를 통과하기 위해 매주 1회씩 오프라인으로 만나 기출문제를 풀고 서로의 생각을 공유하는 스터디입니다.
___

### ✅ 깃헙 Push/Pull 규칙

1. 무조건 __pull__ 먼저 해줍니다. pull을 해서 해당 주차의 디렉토리가 생기지 않는다면 따로 만들어주세요

```
$ git pull <remote 이름> <브랜치이름>
$ git pull origin main
```

2. 다른 사람과 구별될 수 있는 commit 이름으로 push 해주세요
```
$ git add .
$ git commit -m "2week_seonjong"
$ git push origin main
```

3. 기본 설정을 하시면 `git push origin main`을 매번 입력하지 않아도 됩니다.
```
$ git push -u origin main
한번 입력한 이후에는
$ git push
만 입력해주셔도 됩니다!
```

4. 만일 push를 하다가 **에러**가 발생한 경우 아래의 코드를 입력해주세요
```
$ git log --oneline
```

<img width="412" src="https://user-images.githubusercontent.com/97590480/236659877-ebdf7588-4605-4139-a34d-d9e6fe7e1844.png">

빨간색이 최근에 push한 커밋입니다. 여기서 충돌이 났기 때문에 문제가 발생하는데요

밑에 있는 초록색 시점으로 되돌리는 작업을 이용해서 작업 취소를 해줍니다.

입력 후 내가 push한 커밋 바로 전 커밋 코드를 복사해줍니다. 그리고 다음을 입력해주세요
```
$ git reset --soft [복사한 커밋 코드(e.g. 1b9f35b)]
```

### 💕 원격 저장소 등록하기
1. 원하는 디렉토리에 clone해서 다운받습니다. 

```bash
$ git clone https://github.com/Ssunbell/ADP_study
```

2. `git remote add <원격저장소 이름> <주소>` 형식으로 작성합니다.

```bash
$ git remote add origin https://github.com/Ssunbell/ADP_study
```

### 💕 원격 저장소 조회


`git remote -v`로 등록이 잘 됐는지 확인해봅니다.
```
$ git remote -v
origin https://github.com/Ssunbell/ADP_study (fetch)
origin https://github.com/Ssunbell/ADP_study (push)