document.getElementById("quizForm").addEventListener("submit", function(e){
  // 폼 안에 있는 라디오 그룹 이름 목록 추출
  const names = Array.from(new Set(
    Array.from(this.querySelectorAll('input[type="radio"]')).map(r => r.name)
  ));
  // 모든 그룹에 체크가 되었는지 검사
  const allAnswered = names.every(n => this.querySelector(`input[name="${n}"]:checked`));

  if (!allAnswered) {
    e.preventDefault();            // 서버 제출 차단 → 새로고침 없음
    alert("안 푼 문제가 있습니다"); // 브라우저 기본 팝업
    // (선택) 첫 미답변 위치로 스크롤:
    const firstMissing = names.find(n => !this.querySelector(`input[name="${n}"]:checked`));
    if (firstMissing) {
      const el = this.querySelector(`input[name="${firstMissing}"]`);
      el && el.closest('.question')?.scrollIntoView({behavior:'smooth', block:'center'});
    }
  }
});

// :has() 미지원 브라우저 대비
document.querySelectorAll('.options').forEach(group => {
    group.addEventListener('change', e => {
        if (e.target && e.target.type === 'radio') {
        group.querySelectorAll('.option').forEach(o => o.classList.remove('checked'));
        const box = e.target.closest('.option');
        if (box) box.classList.add('checked');
        }
    });
});
