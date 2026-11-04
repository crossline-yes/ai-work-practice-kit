# AI 프로젝트 실습 준비 자료

요구사항을 확인하고, AI와 구현·검증한 뒤 자신의 작업을 설명하는 한국어 학습 자료입니다. **처음에는 [START-HERE.md](START-HERE.md)만 읽으세요.**

이 자료는 직접 만든 범용 학습 자료입니다. 실제 시험 문제·첨부 자료·답안·공식 채점 기준은 포함하지 않습니다. 공개 저장소 Clone 허용만으로 개인이 미리 만든 준비 자료의 시험 중 반입까지 허용된다고 보장할 수는 없습니다. 해당 시험의 운영 안내와 허용 범위를 먼저 확인하세요. 실제 후속 서술형에서는 AI 없이 직접 답하고 자료 열람·복사 제한을 따릅니다.

## 가장 빠른 사용

반입이 허용된 환경의 프로젝트 작업 폴더에서 실행합니다. 이미 `.prep-kit` 폴더가 있으면 덮어쓰지 말고 기존 폴더를 확인하세요.

```sh
git clone --depth 1 https://github.com/crossline-yes/ai-work-practice-kit.git .prep-kit
codex
```

Codex에 처음 보낼 요청:

```text
현재 과제 작업 폴더는 그대로 유지해줘.
.prep-kit/START-HERE.md와 .prep-kit/prompts/01-understand.md를 참고해서,
현재 과제 안내와 제공 자료부터 파악해줘.
과제의 공식 지시와 현재 작업 폴더의 규칙을 우선하고,
이 준비 자료는 범용 참고로만 사용해줘.
확인된 요구사항·파일의 역할·미확인 조건·담당자에게 물어볼 질문 최대 3개를
근거와 함께 쉽게 정리해줘. 아직 구현하거나 파일을 수정하지 마.
```

터미널 명령이 익숙하지 않으면, 허용된 작업용 AI에게 위 Clone 명령의 실행을 요청할 수 있습니다. 경로·권한·네트워크 오류가 나면 오류 내용을 확인하고 제공 환경의 도움말을 따릅니다. 차단을 다른 경로로 우회하지 않습니다.

## 상황별로 꺼내 쓰기

| 지금 할 일 | 읽을 파일 |
|---|---|
| 시작 순서·두 AI의 역할·첫 요청 | [START-HERE.md](START-HERE.md) |
| 원자료와 과제 파악 | [01-understand](prompts/01-understand.md) |
| 담당자에게 질문 | [02-clarify](prompts/02-clarify.md) |
| 요구사항과 구현 계획 | [03-plan](prompts/03-plan.md) |
| 기능 구현 | [04-build](prompts/04-build.md) |
| 실행 오류·계산 오류 | [05-debug](prompts/05-debug.md) |
| 정상·경계·실패·변경 검증 | [06-verify](prompts/06-verify.md) |
| 공개 GitHub 코드 검토 | [07-public-code](prompts/07-public-code.md) |
| 제출물·사용법·남은 작업 | [08-handoff](prompts/08-handoff.md) |
| 연습용 후속 면접 코치 | [09-practice-interview](prompts/09-practice-interview.md) |
| 심층 질문 18개와 답변 연습법 | [deep-followups](study/deep-followups.md) |
| Git 초보용 명령·GitHub 사용법 | [git-guide](docs/git-guide.md) |
| 실행·자료·화면·시간 관리 | [project-manual](docs/project-manual.md) |
| 사용 범위와 시험 중 주의사항 | [use-boundaries](docs/use-boundaries.md) |

## 기록 양식

`templates/`의 빈 양식은 실제 작업 폴더의 `work-notes/`에 복사해 사용합니다. 기록은 각 과제의 자료이므로 공개 학습 저장소에 올리지 마세요.

```sh
python3 .prep-kit/scripts/init_notes.py work-notes
```

Windows에서 `python3`가 없으면 `python` 또는 제공 환경의 실행 명령을 사용하세요. Python이 없으면 작업용 AI에게 템플릿을 복사하도록 요청하면 됩니다. 스크립트는 기존 파일을 덮어쓰지 않습니다.

| 기록 | 남길 내용 |
|---|---|
| `requirements.md` | 요구·근거·미정·완료 기준 |
| `decisions.md` | 내 선택·대안·선택 이유·한계 |
| `verification.md` | 입력·예상·실제·증거·미검증 |
| `delivery.md` | 실행 방법·구현 범위·제출 체크 |
| `ownership.md` | 내 설명·AI 판단 검토·변경 영향 |

## 공개 범위

저장소에는 범용 설명서·직접 만든 요청문·빈 기록 양식만 둡니다. 실제 문제, 업무 파일, 이름·주소, 작업 로그, 완성 답안, 비밀키는 넣지 않습니다. 학습 저장소로의 Push와 실제 시험에서의 작업물 외부 전송은 다릅니다. 시험 중에는 운영 측 전송 제한을 따르세요.

외부 공개 코드의 재사용 조건은 각 저장소의 LICENSE를 별도로 확인합니다. 이 자료 자체의 재사용 조건은 [LICENSE](LICENSE)에 있습니다.
