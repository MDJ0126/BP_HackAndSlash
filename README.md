<div align="center">

# Blade Slash

### Unreal Engine 5 Blueprint Top-Down Hack & Slash

플레이어의 콤보 공격부터 스킬, 적 AI, 전투 UI까지 구현한 탑다운 핵앤슬래시 프로젝트입니다.

![Unreal Engine 5.5](https://img.shields.io/badge/Unreal%20Engine-5.5-0E1128?style=for-the-badge&logo=unrealengine&logoColor=white)
![Blueprint](https://img.shields.io/badge/Blueprint-Visual%20Scripting-137CBD?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-34A853?style=for-the-badge)

<br>

![Blade Slash 플레이 영상](docs/images/blade-slash-gameplay.gif)

</div>

## 게임 다운로드

[BladeSlash.zip 다운로드](https://github.com/MDJ0126/BP_HackAndSlash/blob/main/BladeSlash.zip?raw=true)

압축 해제 후, `BP_HackAndSlash.exe`를 실행하여 플레이할 수 있습니다.

## 프로젝트 개요

| 항목 | 내용 |
| --- | --- |
| 개발 기간 | 2026.08.25 ~ 2026.09.02 (약 1주) |
| 개발 형태 | 기획 및 클라이언트 1인 개발 |
| 장르 | 탑다운 핵앤슬래시 |
| 엔진 | Unreal Engine 5.5 |
| 기술 | Blueprint, Behavior Tree, Niagara, Enhanced Input |
| 형상 관리 | Git, GitHub LFS |

플레이어 입력, 공격 판정, 적의 반응과 AI 행동, 이펙트 및 UI를 개발했습니다. 공통 캐릭터를 상속해 플레이어와 적을 구성하고, 캐릭터 및 스킬 정보는 데이터 테이블에서 관리합니다.

## 주요 구현

### 전투 및 스킬

- 공격 애니메이션을 연계한 연속 공격과 콤보 시스템
- Animation Notify 기반의 전방 박스·구체 공격 판정
- 일반 공격, 회전 베기, 순간 이동 궁극기
- 원형·사각형 스킬 범위 가이드
- 검 궤적, 피격 이펙트, 카메라 셰이크와 사망 래그돌

### 적 AI

- Behavior Tree 기반 감지·순찰·추적·공격 행동
- Blackboard와 BT Service를 이용한 감지 여부, 공격 거리, AI 상태 관리
- 근접 미니언과 투사체를 발사하는 원거리 미니언

### 데이터 및 UI

- 체력 바, 콤보 카운트, 스킬 슬롯과 적 이름표
- Data Table 기반 캐릭터·스킬 정보 관리
- Enhanced Input 기반 플레이어 입력 구성

## 구조

```text
BP_Character                       # 공통 체력 및 피격 처리
├─ BP_Player                       # 플레이어 전투 기능
│  └─ BP_Kwang                    # 실제 플레이어블 캐릭터
└─ BP_Enemy                        # 적 공통 기능
   ├─ BP_Minion_Melee             # 근거리 미니언
   └─ BP_Minion_Siege             # 원거리 미니언

BP_EnemyController
├─ BB_Enemy                        # AI 상태 데이터
└─ BT_Enemy                        # 감지·순찰·추적·공격 전환

DT_Character                       # 캐릭터 데이터
└─ DT_Skill                        # 스킬 데이터
```

공격 몽타주의 Notify 구간에서 판정과 투사체 발사를 실행해 애니메이션의 타격 시점과 실제 공격 처리를 맞췄습니다. 플레이어와 적이 공유하는 체력·피격 처리는 `BP_Character`에 두고, 각 캐릭터에 필요한 전투 기능은 자식 Blueprint에서 구현했습니다.
