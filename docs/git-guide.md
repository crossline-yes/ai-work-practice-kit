# Git과 GitHub 사용 설명서

Git은 변경 이력을 기록하는 도구이고 GitHub는 저장소를 온라인으로 보관·공유하는 서비스입니다. Clone은 가져오기, Commit은 내 작업 공간에 기록하기, Push는 외부 저장소로 보내기입니다.

## 자료 가져오기

사용이 허용된 프로젝트 폴더에서 실행합니다.

```sh
git clone --depth 1 https://github.com/crossline-yes/ai-work-practice-kit.git .prep-kit
```

인증이 필요 없는 공개 저장소입니다. 이미 대상 폴더가 있으면 새로 Clone하지 말고 내용을 확인합니다. README.md는 GitHub 화면에서도 읽을 수 있지만, 실제 시험에서는 외부 브라우저 접속 제한을 따릅니다.

## Git을 모를 때 AI에 맡기기

```text
현재 과제 폴더의 Git 상태를 확인해줘.
수정·추가된 파일과 변경 내용을 요약하고, 내가 직접 볼 핵심 차이를 알려줘.
원격 전송이나 이력 재작성, 파일 삭제는 하지 마.
```

## 작업을 확인하는 명령

아래는 연습·개발용 사용법입니다. 시험에서의 허용 명령과 도구 제한을 확인하세요.

```sh
git status --short
git diff
git diff --cached
git log --oneline -5
```

- `status`: 수정·추가·미추적 파일 확인.
- `diff`: 아직 스테이징하지 않은 변경. 미추적 새 파일의 내용은 기본 diff에 나오지 않으므로 status도 확인합니다.
- `diff --cached`: 다음 Commit에 포함할 변경.
- `log`: 최근 기록.

다른 폴더를 지정하려면 `git -C "프로젝트폴더" status --short`처럼 사용합니다. `.prep-kit` 저장소의 이력과 실제 과제 프로젝트의 이력은 별개입니다.

## 연습에서 변경을 기록하기

원래 Git 저장소인지 먼저 확인하세요. 새 연습 프로젝트에만 필요한 경우 `git init`을 사용합니다. 기존 저장소의 설정을 임의로 바꾸지 않습니다.

```sh
git add -- "검토한파일1" "검토한파일2"
git diff --cached
git commit -m "설명 가능한 변경 내용"
```

위 파일명은 실제 확인한 파일명으로 바꿉니다. Commit은 GitHub 업로드가 아닙니다. 작성자 설정을 요구하면 본인 정보를 확인해 해당 저장소에만 설정합니다. 무작정 `git add .`로 비밀키·원자료·로그까지 포함시키지 마세요. 되돌리기가 필요하면 작업용 AI에게 미저장·미커밋 변경을 먼저 확인시키고 안전한 방법을 설명받습니다.

## 시험에서는 외부 전송을 구분

이 학습 저장소로 과제 결과를 Push하지 마세요. 공개 자료를 가져올 수 있다는 사실과 문제·첨부 파일·작업물을 밖으로 보낼 수 있다는 사실은 다릅니다. 이 문서는 시험 중 Push나 로컬 Commit의 허용을 대신 결정하지 않습니다.

## 공식 참고

- [Clone](https://git-scm.com/docs/git-clone)
- [Git 및 -C](https://git-scm.com/docs/git)
- [Status](https://git-scm.com/docs/git-status)
- [Diff](https://git-scm.com/docs/git-diff)
- [Log](https://git-scm.com/docs/git-log)
- [GitHub 저장소 라이선스](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
