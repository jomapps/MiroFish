<template>
  <div class="home-container fade-in">
    <!-- Navbar -->
    <nav class="navbar glass">
      <div class="nav-brand">MIROFISH</div>
      <div class="nav-links">
        <a href="https://github.com/666ghj/MiroFish" target="_blank" class="github-link">
          REHEARSE THE FUTURE <span class="arrow">↗</span>
        </a>
      </div>
    </nav>

    <div class="main-content">
      <!-- Hero Section -->
      <section class="hero-section">
        <div class="hero-left">
          <div class="tag-row">
            <span class="orange-tag">SWARM INTELLIGENCE ENGINE</span>
            <span class="version-text">/ v0.1 PREVIEW</span>
          </div>
          
          <h1 class="main-title">
            Analyze Seeds.<br>
            <span class="gradient-text">Predict Anything.</span>
          </h1>
          
          <div class="hero-desc">
            <p>
              Even with a single paragraph, <span class="highlight-bold">MiroFish</span> architect parallel worlds with up to <span class="highlight-orange">1,000,000 Agents</span>. Inject variables from a God's-eye view to discover <span class="highlight-code">local optimal solutions</span> in complex social simulations.
            </p>
            <p class="slogan-text">
              Rehearse the future in digital sandboxes and win decisions after countless simulations.<span class="blinking-cursor">_</span>
            </p>
          </div>
        </div>
        
        <div class="hero-right">
          <div class="logo-container glass-card">
            <img src="../assets/logo/MiroFish_logo_left.jpeg" alt="MiroFish Logo" class="hero-logo" />
          </div>
          
          <button class="scroll-down-btn" @click="scrollToBottom">
            SCROLL <span class="btn-arrow">↓</span>
          </button>
        </div>
      </section>

      <!-- Dashboard Section -->
      <section class="dashboard-section grid-2">
        <!-- Left: Status & Workflow -->
        <div class="left-panel glass-card">
          <div class="panel-header">
            <span class="status-dot">■</span> SYSTEM STATUS: READY
          </div>
          
          <h2 class="section-title">Engine Idling</h2>
          <p class="section-desc">
            The prediction engine is on standby. Upload unstructured data reports to initialize a simulation sequence.
          </p>
          
          <div class="metrics-row">
            <div class="metric-card glass">
              <div class="metric-value">EFFICIENCY</div>
              <div class="metric-label">Avg. $5 per simulation</div>
            </div>
            <div class="metric-card glass">
              <div class="metric-value">SCALE</div>
              <div class="metric-label">Up to 1M Agent Simulation</div>
            </div>
          </div>

          <div class="steps-container">
            <div class="steps-header">
               <span class="diamond-icon">◇</span> WORKFLOW SEQUENCE
            </div>
            <div class="workflow-list">
              <div class="workflow-item">
                <span class="step-num">01</span>
                <div class="step-info">
                  <div class="step-title">Knowledge Graph Construction</div>
                  <div class="step-desc">Extracting reality seeds & injecting collective memories & GraphRAG building.</div>
                </div>
              </div>
              <div class="workflow-item">
                <span class="step-num">02</span>
                <div class="step-info">
                  <div class="step-title">Environment Setup</div>
                  <div class="step-desc">Entity extraction & profile generation & simulation parameter injection.</div>
                </div>
              </div>
              <div class="workflow-item">
                <span class="step-num">03</span>
                <div class="step-info">
                  <div class="step-title">Start Simulation</div>
                  <div class="step-desc">Dual-platform parallel simulation with dynamic temporal memory updates.</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right: Console -->
        <div class="right-panel glass-card">
          <div class="console-box">
            <div class="console-section">
              <div class="console-header">
                <span class="console-label">01 / REALITY SEEDS</span>
                <span class="console-meta">PDF, MD, TXT</span>
              </div>
              
              <div 
                class="upload-zone glass"
                :class="{ 'drag-over': isDragOver, 'has-files': files.length > 0 }"
                @dragover.prevent="handleDragOver"
                @dragleave.prevent="handleDragLeave"
                @drop.prevent="handleDrop"
                @click="triggerFileInput"
              >
                <input
                  ref="fileInput"
                  type="file"
                  multiple
                  accept=".pdf,.md,.txt"
                  @change="handleFileSelect"
                  style="display: none"
                  :disabled="loading"
                />
                
                <div v-if="files.length === 0" class="upload-placeholder">
                  <div class="upload-icon">↑</div>
                  <div class="upload-title">Drop Reports Here</div>
                  <div class="upload-hint">or click to browse filesystem</div>
                </div>
                
                <div v-else class="file-list">
                  <div v-for="(file, index) in files" :key="index" class="file-item glass">
                    <span class="file-icon">📄</span>
                    <span class="file-name">{{ file.name }}</span>
                    <button @click.stop="removeFile(index)" class="remove-btn">×</button>
                  </div>
                </div>
              </div>
            </div>

            <div class="console-divider">
              <span>SIMULATION PARAMETERS</span>
            </div>

            <div class="console-section">
              <div class="console-header">
                <span class="console-label">>_ 02 / PROMPT</span>
              </div>
              <div class="input-wrapper glass">
                <textarea
                  v-model="formData.simulationRequirement"
                  class="code-input"
                  placeholder="// Enter simulation or prediction requirements in natural language (e.g., What if the policy changes?)"
                  rows="6"
                  :disabled="loading"
                ></textarea>
                <div class="model-badge">ENGINE: MIROFISH-V1.0</div>
              </div>
            </div>

            <div class="console-section btn-section">
              <button 
                class="btn-premium start-engine-btn"
                @click="startSimulation"
                :disabled="!canSubmit || loading"
              >
                <span v-if="!loading">START ENGINE</span>
                <span v-else>INITIALIZING...</span>
                <span class="btn-arrow">→</span>
              </button>
            </div>
          </div>
        </div>
      </section>

      <!-- History Section -->
      <HistoryDatabase />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import HistoryDatabase from '../components/HistoryDatabase.vue'

const router = useRouter()

// 表单数据
const formData = ref({
  simulationRequirement: ''
})

// Files
const files = ref([])

// 状态
const loading = ref(false)
const error = ref('')
const isDragOver = ref(false)

// 文件输入引用
const fileInput = ref(null)

// 计算属性:是否可以提交
const canSubmit = computed(() => {
  return formData.value.simulationRequirement.trim() !== '' && files.value.length > 0
})

// 触发文件选择
const triggerFileInput = () => {
  if (!loading.value) {
    fileInput.value?.click()
  }
}

// 处理文件选择
const handleFileSelect = (event) => {
  const selectedFiles = Array.from(event.target.files)
  addFiles(selectedFiles)
}

// 处理拖拽相关
const handleDragOver = (e) => {
  if (!loading.value) {
    isDragOver.value = true
  }
}

const handleDragLeave = (e) => {
  isDragOver.value = false
}

const handleDrop = (e) => {
  isDragOver.value = false
  if (loading.value) return
  
  const droppedFiles = Array.from(e.dataTransfer.files)
  addFiles(droppedFiles)
}

// 添加文件
const addFiles = (newFiles) => {
  const validFiles = newFiles.filter(file => {
    const ext = file.name.split('.').pop().toLowerCase()
    return ['pdf', 'md', 'txt'].includes(ext)
  })
  files.value.push(...validFiles)
}

// 移除文件
const removeFile = (index) => {
  files.value.splice(index, 1)
}

// 滚动到底部
const scrollToBottom = () => {
  window.scrollTo({
    top: document.body.scrollHeight,
    behavior: 'smooth'
  })
}

// Start Simulation - 立即跳转，API调用在Process页面进行
const startSimulation = () => {
  if (!canSubmit.value || loading.value) return
  
  // 存储待上传的数据
  import('../store/pendingUpload.js').then(({ setPendingUpload }) => {
    setPendingUpload(files.value, formData.value.simulationRequirement)
    
    // 立即跳转到Process页面（使用特殊标识表示新建项目）
    router.push({
      name: 'Process',
      params: { projectId: 'new' }
    })
  })
}
</script>

<style scoped>
.home-container {
  min-height: 100vh;
  background: var(--bg-dark);
  font-family: var(--font-mono);
  color: var(--text-primary);
}

/* Navbar */
.navbar {
  height: 70px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 60px;
  position: sticky;
  top: 0;
  z-index: 100;
  margin: 20px 40px;
}

.nav-brand {
  font-weight: 800;
  letter-spacing: 2px;
  font-size: 1.4rem;
  background: var(--accent-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.github-link {
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 1px;
  transition: color 0.3s;
}

.github-link:hover {
  color: var(--primary);
}

/* Main Content */
.main-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 40px 60px;
}

/* Hero Section */
.hero-section {
  display: flex;
  justify-content: space-between;
  margin-bottom: 100px;
  min-height: 60vh;
  align-items: center;
}

.hero-left {
  flex: 1.2;
  padding-right: 80px;
}

.tag-row {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 30px;
  font-size: 0.75rem;
}

.orange-tag {
  background: var(--primary);
  color: white;
  padding: 4px 12px;
  font-weight: 800;
  letter-spacing: 1.5px;
}

.version-text {
  color: var(--text-secondary);
  font-weight: 500;
}

.main-title {
  font-size: 5rem;
  line-height: 1.1;
  font-weight: 700;
  margin: 0 0 45px 0;
  letter-spacing: -3px;
}

.gradient-text {
  background: var(--accent-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-desc {
  font-size: 1.1rem;
  line-height: 1.8;
  color: var(--text-secondary);
  max-width: 650px;
  margin-bottom: 60px;
}

.highlight-bold {
  color: var(--text-primary);
  font-weight: 600;
}

.highlight-orange {
  color: var(--primary);
  font-weight: 700;
}

.highlight-code {
  background: rgba(255, 255, 255, 0.1);
  padding: 2px 8px;
  border-radius: 4px;
  color: var(--primary);
}

.slogan-text {
  font-size: 1.3rem;
  font-weight: 500;
  color: var(--text-primary);
  border-left: 4px solid var(--primary);
  padding-left: 20px;
  margin-top: 30px;
}

.blinking-cursor {
  color: var(--primary);
  animation: blink 1s step-end infinite;
}

.hero-right {
  flex: 0.8;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 40px;
}

.logo-container {
  width: 100%;
  padding: 20px;
  display: flex;
  justify-content: center;
}

.hero-logo {
  max-width: 100%;
  height: auto;
  filter: grayscale(0.2) contrast(1.1);
  border-radius: 8px;
}

.scroll-down-btn {
  background: transparent;
  border: 1px solid var(--glass-border);
  color: var(--text-secondary);
  padding: 10px 20px;
  font-size: 0.8rem;
  cursor: pointer;
  transition: all 0.3s;
  border-radius: 20px;
  letter-spacing: 2px;
}

.scroll-down-btn:hover {
  border-color: var(--primary);
  color: var(--primary);
}

/* Dashboard */
.dashboard-section {
  padding-top: 80px;
  border-top: 1px solid var(--glass-border);
}

.left-panel, .right-panel {
  padding: 40px;
}

.panel-header {
  font-size: 0.75rem;
  color: var(--text-secondary);
  letter-spacing: 2px;
  margin-bottom: 30px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.status-dot {
  color: var(--primary);
}

.section-title {
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.section-desc {
  color: var(--text-secondary);
  margin-bottom: 40px;
  line-height: 1.6;
}

.metrics-row {
  display: flex;
  gap: 20px;
  margin-bottom: 40px;
}

.metric-card {
  padding: 25px;
  flex: 1;
}

.metric-value {
  font-size: 1.4rem;
  font-weight: 700;
  margin-bottom: 8px;
  color: var(--primary);
}

.metric-label {
  font-size: 0.8rem;
  color: var(--text-secondary);
}

.steps-container {
  margin-top: 40px;
}

.steps-header {
  font-size: 0.8rem;
  color: var(--text-secondary);
  margin-bottom: 30px;
  letter-spacing: 1px;
}

.workflow-item {
  display: flex;
  gap: 24px;
  margin-bottom: 30px;
}

.step-num {
  font-size: 1.2rem;
  font-weight: 800;
  opacity: 0.2;
}

.step-title {
  font-weight: 600;
  font-size: 1.1rem;
  margin-bottom: 6px;
}

.step-desc {
  font-size: 0.9rem;
  color: var(--text-secondary);
}

/* Console */
.console-box {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.console-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 15px;
  font-size: 0.75rem;
}

.upload-zone {
  height: 220px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s;
}

.upload-zone:hover {
  border-color: var(--primary);
  background: rgba(255, 69, 0, 0.05);
}

.upload-icon {
  font-size: 2rem;
  color: var(--primary);
  margin-bottom: 15px;
}

.upload-title {
  font-weight: 600;
  margin-bottom: 5px;
}

.upload-hint {
  font-size: 0.75rem;
  color: var(--text-secondary);
}

.console-divider {
  display: flex;
  align-items: center;
  gap: 20px;
  margin: 10px 0;
}

.console-divider::before, .console-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--glass-border);
}

.console-divider span {
  font-size: 0.7rem;
  color: var(--text-secondary);
  letter-spacing: 2px;
}

.input-wrapper {
  padding: 15px;
  position: relative;
}

.code-input {
  width: 100%;
  background: transparent;
  border: none;
  color: var(--text-primary);
  font-family: var(--font-mono);
  font-size: 0.95rem;
  resize: none;
  outline: none;
}

.model-badge {
  position: absolute;
  bottom: 15px;
  right: 15px;
  font-size: 0.7rem;
  color: var(--text-secondary);
  background: rgba(0,0,0,0.3);
  padding: 2px 8px;
  border-radius: 4px;
}

.start-engine-btn {
  width: 100%;
  background: var(--black);
  color: var(--white);
  border: none;
  padding: 20px;
  font-family: var(--font-mono);
  font-weight: 700;
  font-size: 1.1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s ease;
  letter-spacing: 1px;
  position: relative;
  overflow: hidden;
}

/* 可点击状态（非禁用） */
.start-engine-btn:not(:disabled) {
  background: var(--black);
  border: 1px solid var(--black);
  animation: pulse-border 2s infinite;
}

.start-engine-btn:hover:not(:disabled) {
  background: var(--orange);
  border-color: var(--orange);
  transform: translateY(-2px);
}

.start-engine-btn:active:not(:disabled) {
  transform: translateY(0);
}

.start-engine-btn:disabled {
  background: #E5E5E5;
  color: #999;
  cursor: not-allowed;
  transform: none;
  border: 1px solid #E5E5E5;
}

/* 引导动画：微妙的边框脉冲 */
@keyframes pulse-border {
  0% { box-shadow: 0 0 0 0 rgba(0, 0, 0, 0.2); }
  70% { box-shadow: 0 0 0 6px rgba(0, 0, 0, 0); }
  100% { box-shadow: 0 0 0 0 rgba(0, 0, 0, 0); }
}

/* 响应式适配 */
@media (max-width: 1024px) {
  .dashboard-section {
    flex-direction: column;
  }
  
  .hero-section {
    flex-direction: column;
  }
  
  .hero-left {
    padding-right: 0;
    margin-bottom: 40px;
  }
  
  .hero-logo {
    max-width: 200px;
    margin-bottom: 20px;
  }
}
</style>
