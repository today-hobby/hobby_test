// /static/home.js
document.addEventListener('DOMContentLoaded', function () {
  const holder = document.getElementById('rec');
  if (!holder) return;

  const mbti = holder.dataset.mbti;

  // 예시 매핑 (원하는 취미/카피로 바꿔도 됨)
  const RECS = {
    'CAF': {
      heroTitle: "모험적 성취가",
      typeLong: "CAF : Consumer Active Focused",
      typeDesc: "다양한 경험에 과감히 투자하며<br>몰입과 에너지를 쏟아 성취를 이뤄내는 사람<br>도전 속에서 성장을 추구",
      items: ['자전거 타기', '실내 스포츠 (클라이밍, 수영, 볼링, 당구, 탁구, 배드민턴)', '실외 스포츠 (스케이트, 스키/보드, 야구)', '방탈출', '요리/베이킹', '코스프레', '필라테스']
    },
    'MPR': {
      heroTitle: "사색형 관찰자",
      typeLong: "MPR : Minimal Passive Relaxed",
      typeDesc: "혼자만의 시간을 통해 세상을 해석하고 기록하는 사람<br>활동보다는 조용한 취미를 즐기며<br>주변을 세심하게 관찰해 의미 부여",
      items: ['유튜브 시청', '라디오 듣기', '독서', '웹툰 보기', '만화책 보기', '사진 찍기', '노래 듣기', 'SNS 활동']
    },
    'MAR': {
      heroTitle: "자유의 탐험가",
      typeLong: "MAR : Minimal Active Relaxed",
      typeDesc: "새로운 것을 찾아 떠나는 것을 좋아하지만<br>느긋한 마음으로 여유를 즐기는 사람<br>소비보다 경험, 계획 없이 하는 편안한 탐험을 선호",
      items: ['산책', '등산', '아이쇼핑', '플리마켓/벼룩시장 구경하기', '팝업스토어 방문', '브이로그 촬영', '봉사활동']
    },
    'CPR': {
      heroTitle: "감각적 미식가",
      typeLong: "CPR : Consumer Passive Relaxed",
      typeDesc: "필요한 순간에 기꺼이 소비해 만족을 추구하는 사람<br>느긋한 일상 속에서 카페, 맛집, 소품 쇼핑처럼<br>감각을 채우는 즐거움을 탐색",
      items: ['OTT 시청', '덕질 (굿즈 모으기, 팬카페 활동 등)', '플라워 클래스','다꾸 (다이어리 꾸미기/캘린더 꾸미기)', '수집 (피규어, 스티커 등등)', '향수 수집', '사진 인화/앨범 만들기', '식물 키우기']
    },
    'CAR': {
      heroTitle: "적극적 모험가",
      typeLong: "CAR : Consumer Active Relaxed",
      typeDesc: "새로운 경험에 시간과 돈을 아끼지 않는 사람<br>활발한 활동과 느슨한 계획 속에서 자유를 만끽하며<br>순간의 즐거움이 중요",
      items: ['노래방 가기', '쇼핑', '맛집 탐방', '카페 투어', '여행 (도시 탐방/스탬프 투어/지역축제)', '캠핑', '스포츠 관람 (야구 관람)', '콘서트/연극 관람', '미술관/전시회/뮤지컬 관람', '방 꾸미기']
    },
    'MAF': {
      heroTitle: "몰입형 창작자",
      typeLong: "MAF : Minimal Active Focused",
      typeDesc: "한 번 시작한 일에는 깊이 빠져드는 사람<br>물질적 소비보다 자신이 만든 결과물에서 성취감을 느끼며<br>완성도를 위해 끝까지 몰두",
      items: ['홈트레이닝', '요가', '춤 배우기', '마라톤 참가']
    },
    'MPF': {
      heroTitle: "사색형 장인",
      typeLong: "MPF : Minimal Passive Focused",
      typeDesc: "차분한 공간에서 깊이 탐구하는 것을 즐기는 사람<br>화려함보단 내실, 오랜 시간 쌓인 노하우로 완성도의 극대화",
      items: ['게임하기 (PC/콘솔/모바일)', '캘리그래피', '그림 그리기', '종이접기', '글쓰기(일기)', '리폼(의류, 소품)', '명상']
    },
    'CPF': {
      heroTitle: "정교한 수집가",
      typeLong: "CPF : Consumer Passive Focused",
      typeDesc: "마음을 끄는 분야에 기꺼이 투자하는 사람<br>세밀한 관심과 집중력으로 취미를 예술의 경지로 완성",
      items: ['보드게임', '인형 뽑기', '공예 (비즈, 가죽, 우드, 도예 등)', '뜨개질/자수', '디지털 드로잉', '레고/프라모델 조립', '퍼즐 맞추기', '악기 배우기 (피아노, 기타 등)', '자기계발 (자격증, 온라인 클래스 듣기)']
    }
    // ... 필요한 조합 계속 추가
  };

  const data = RECS[mbti];
  if (!data) return;

  document.querySelector('.hero-title').innerHTML = data.heroTitle;
  document.querySelector('.type-long').innerHTML = data.typeLong;
  document.querySelector('.type-desc').innerHTML = data.typeDesc;

  const listHTML = data.items
    .map(item => `<li class="rec-item">${item}</li>`)
    .join('');

  holder.innerHTML = listHTML;
});
