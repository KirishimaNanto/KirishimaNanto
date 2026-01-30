<!-- ================= 人格状态面板 · MIO ================= -->

<p align="center">
  <svg width="900" height="260" viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg">

    <defs>
      <!-- 背景渐变（MIO 粉蓝） -->
      <linearGradient id="mioBg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#FADADD"/>
        <stop offset="100%" stop-color="#C7EDE6"/>
      </linearGradient>

      <!-- 波形渐变 -->
      <linearGradient id="mioWave" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#7EC8E3"/>
        <stop offset="50%" stop-color="#F4A6C1"/>
        <stop offset="100%" stop-color="#7EC8E3"/>
      </linearGradient>

      <!-- 发光 -->
      <filter id="softGlow">
        <feGaussianBlur stdDeviation="3" result="blur"/>
        <feMerge>
          <feMergeNode in="blur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    </defs>

    <!-- 背景 -->
    <rect x="0" y="0" width="900" height="260" rx="28" fill="url(#mioBg)" />

    <!-- 波形 -->
    <path
      d="
        M 0 150
        C 60 120, 120 180, 180 150
        C 240 120, 300 180, 360 150
        C 420 120, 480 180, 540 150
        C 600 120, 660 180, 720 150
        C 780 120, 840 180, 900 150
      "
      fill="none"
      stroke="url(#mioWave)"
      stroke-width="6"
      filter="url(#softGlow)"
    />

    <!-- 标题 -->
    <text x="450" y="95"
      text-anchor="middle"
      font-size="26"
      fill="#4B6E8A"
      font-family="sans-serif">
      現在人格状態 · MIO
    </text>

    <!-- 副标题 -->
    <text x="450" y="130"
      text-anchor="middle"
      font-size="18"
      fill="#5A8FA8"
      font-family="sans-serif">
      月城 澪 · Pastel Execution Mode
    </text>

    <!-- 状态 -->
    <text x="450" y="200"
      text-anchor="middle"
      font-size="14"
      fill="#5A8FA8"
      font-family="monospace">
      Calm · Precise · Always Watching Your Schedule
    </text>

  </svg>
</p>

---

## 🧠 Persona Card

**Name**  
月城 澪 / MIO

**Role**  
Schedule Engineer × Soft AI

**Color Theme**  
Pastel Blue × Soft Pink

**Wave Pattern**  
Low-frequency · Stable · Emotion-buffered

**Status**  
Active · Syncing · Background Support

---

> この Repo は「MIO 人格」が管理しています。  
> 処理は静か、判断は正確、感情は少しだけ。
