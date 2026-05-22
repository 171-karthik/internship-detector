<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>InternShield – Fake Internship Detection System</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
:root {
  --purple: #7c3aed;
  --purple-light: #a78bfa;
  --purple-dark: #4c1d95;
  --cyan: #06b6d4;
  --cyan-light: #67e8f9;
  --blue: #3b82f6;
  --blue-dark: #1d4ed8;
  --pink: #ec4899;
  --green: #10b981;
  --amber: #f59e0b;
  --red: #ef4444;
  --orange: #f97316;
  --dark: #0f0a1e;
  --dark2: #1a1033;
  --dark3: #251842;
  --card-bg: rgba(255,255,255,0.05);
  --glass: rgba(255,255,255,0.08);
  --border: rgba(255,255,255,0.12);
  --text: #f0e6ff;
  --text-muted: #9d89c4;
}
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:'DM Sans',sans-serif; background:var(--dark); color:var(--text); overflow-x:hidden; }

/* NAV */
nav { position:fixed; top:0; left:0; right:0; z-index:100; background:rgba(15,10,30,0.85); backdrop-filter:blur(20px); border-bottom:1px solid var(--border); padding:0 2rem; display:flex; align-items:center; justify-content:space-between; height:64px; }
.logo { font-family:'Syne',sans-serif; font-size:1.4rem; font-weight:800; background:linear-gradient(135deg,var(--cyan),var(--purple)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.nav-links { display:flex; gap:2rem; align-items:center; }
.nav-links a { color:var(--text-muted); text-decoration:none; font-size:0.9rem; font-weight:500; transition:color 0.2s; cursor:pointer; }
.nav-links a:hover, .nav-links a.active { color:var(--text); }
.btn-nav { background:linear-gradient(135deg,var(--purple),var(--blue)); padding:0.5rem 1.25rem; border-radius:8px; color:#fff!important; font-size:0.85rem!important; border:none; cursor:pointer; }

/* PAGES */
.page { display:none; min-height:100vh; }
.page.active { display:block; }

/* LANDING */
#landing { background:radial-gradient(ellipse 80% 60% at 50% -10%, rgba(124,58,237,0.4) 0%, transparent 60%), var(--dark); }

/* HERO */
.hero { padding:140px 4rem 80px; text-align:center; max-width:1100px; margin:0 auto; }
.hero-badge { display:inline-flex; align-items:center; gap:8px; background:rgba(124,58,237,0.2); border:1px solid rgba(124,58,237,0.4); border-radius:50px; padding:6px 16px; font-size:0.8rem; color:var(--purple-light); margin-bottom:2rem; }
.hero-badge span { width:6px; height:6px; border-radius:50%; background:var(--cyan); animation:pulse 2s infinite; }
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.5;transform:scale(1.5)} }
h1.hero-title { font-family:'Syne',sans-serif; font-size:clamp(2.5rem,6vw,4.5rem); font-weight:800; line-height:1.1; margin-bottom:1.5rem; }
.grad-text { background:linear-gradient(135deg,var(--cyan) 0%,var(--purple-light) 50%,var(--pink) 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.hero p { font-size:1.15rem; color:var(--text-muted); max-width:600px; margin:0 auto 2.5rem; line-height:1.7; }
.hero-btns { display:flex; gap:1rem; justify-content:center; flex-wrap:wrap; }
.btn-primary { background:linear-gradient(135deg,var(--purple),var(--blue)); color:#fff; border:none; padding:0.9rem 2rem; border-radius:12px; font-size:1rem; font-weight:600; cursor:pointer; transition:transform 0.2s,box-shadow 0.2s; font-family:'DM Sans',sans-serif; }
.btn-primary:hover { transform:translateY(-2px); box-shadow:0 10px 40px rgba(124,58,237,0.4); }
.btn-outline { background:transparent; color:var(--text); border:1px solid var(--border); padding:0.9rem 2rem; border-radius:12px; font-size:1rem; font-weight:600; cursor:pointer; transition:all 0.2s; font-family:'DM Sans',sans-serif; }
.btn-outline:hover { border-color:var(--purple-light); background:rgba(124,58,237,0.1); }

/* STATS STRIP */
.stats-strip { display:grid; grid-template-columns:repeat(4,1fr); gap:1px; background:var(--border); margin:0 4rem; border-radius:16px; overflow:hidden; }
.stat-item { background:var(--dark2); padding:1.5rem 2rem; text-align:center; }
.stat-num { font-family:'Syne',sans-serif; font-size:2rem; font-weight:800; background:linear-gradient(135deg,var(--cyan),var(--purple)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.stat-label { font-size:0.8rem; color:var(--text-muted); margin-top:4px; }

/* FEATURES */
.section { padding:80px 4rem; max-width:1200px; margin:0 auto; }
.section-label { font-size:0.8rem; text-transform:uppercase; letter-spacing:0.15em; color:var(--cyan); font-weight:600; margin-bottom:1rem; }
.section-title { font-family:'Syne',sans-serif; font-size:2.2rem; font-weight:700; margin-bottom:1rem; }
.section-sub { color:var(--text-muted); font-size:1rem; max-width:500px; line-height:1.7; }
.features-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem; margin-top:3rem; }
.feature-card { background:var(--glass); border:1px solid var(--border); border-radius:20px; padding:2rem; transition:all 0.3s; position:relative; overflow:hidden; }
.feature-card::before { content:''; position:absolute; inset:0; background:linear-gradient(135deg,var(--glow-start,rgba(124,58,237,0.05)),transparent); opacity:0; transition:opacity 0.3s; }
.feature-card:hover { border-color:rgba(124,58,237,0.4); transform:translateY(-4px); }
.feature-card:hover::before { opacity:1; }
.feature-icon { width:48px; height:48px; border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:1.5rem; margin-bottom:1.25rem; }
.feature-card h3 { font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; margin-bottom:0.75rem; }
.feature-card p { color:var(--text-muted); font-size:0.9rem; line-height:1.6; }

/* SCAM AWARENESS */
.scam-section { background:linear-gradient(135deg,rgba(239,68,68,0.08),rgba(249,115,22,0.08)); border:1px solid rgba(239,68,68,0.2); border-radius:24px; padding:3rem; margin:0 4rem; }
.scam-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:2rem; margin-top:2rem; }
.scam-item { display:flex; gap:1rem; align-items:flex-start; }
.scam-dot { width:8px; height:8px; border-radius:50%; background:var(--red); margin-top:6px; flex-shrink:0; }
.scam-item p { font-size:0.9rem; color:var(--text-muted); line-height:1.6; }
.scam-item strong { color:var(--text); }

/* TESTIMONIALS */
.testimonials-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem; margin-top:3rem; }
.testimonial-card { background:var(--glass); border:1px solid var(--border); border-radius:20px; padding:1.75rem; }
.stars { color:var(--amber); font-size:0.9rem; margin-bottom:1rem; }
.testimonial-card p { color:var(--text-muted); font-size:0.9rem; line-height:1.7; margin-bottom:1.25rem; }
.t-author { display:flex; align-items:center; gap:12px; }
.t-avatar { width:36px; height:36px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:0.8rem; }
.t-name { font-size:0.85rem; font-weight:600; }
.t-role { font-size:0.75rem; color:var(--text-muted); }

/* FOOTER */
footer { border-top:1px solid var(--border); padding:3rem 4rem; text-align:center; color:var(--text-muted); font-size:0.85rem; }
footer .foot-logo { font-family:'Syne',sans-serif; font-size:1.5rem; font-weight:800; background:linear-gradient(135deg,var(--cyan),var(--purple)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:1rem; }

/* FORM PAGE */
#analysis { background:radial-gradient(ellipse 60% 50% at 30% 20%, rgba(6,182,212,0.15) 0%, transparent 50%), radial-gradient(ellipse 60% 50% at 70% 80%, rgba(124,58,237,0.15) 0%, transparent 50%), var(--dark); padding-top:80px; min-height:100vh; }
.form-container { max-width:900px; margin:0 auto; padding:4rem 2rem; }
.form-header { text-align:center; margin-bottom:3rem; }
.form-card { background:var(--glass); border:1px solid var(--border); border-radius:24px; padding:3rem; }
.form-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:1.5rem; }
.form-group { display:flex; flex-direction:column; gap:8px; }
.form-group.full { grid-column:1/-1; }
label { font-size:0.85rem; font-weight:500; color:var(--text-muted); }
input, select, textarea { background:rgba(255,255,255,0.06); border:1px solid var(--border); border-radius:10px; padding:0.75rem 1rem; color:var(--text); font-family:'DM Sans',sans-serif; font-size:0.95rem; transition:border-color 0.2s; width:100%; }
input:focus, select:focus, textarea:focus { outline:none; border-color:var(--purple-light); background:rgba(124,58,237,0.08); }
select option { background:var(--dark2); }
textarea { resize:vertical; min-height:100px; }
.risk-meter-preview { background:rgba(255,255,255,0.04); border:1px solid var(--border); border-radius:12px; padding:1.25rem; margin-top:1rem; }
.risk-meter-label { font-size:0.8rem; color:var(--text-muted); margin-bottom:0.75rem; }
.risk-bar-bg { background:rgba(255,255,255,0.08); border-radius:50px; height:8px; overflow:hidden; }
.risk-bar-fill { height:100%; border-radius:50px; background:linear-gradient(90deg,var(--green),var(--amber),var(--red)); width:0%; transition:width 0.8s cubic-bezier(0.34,1.56,0.64,1); }
.btn-analyze { width:100%; margin-top:2rem; padding:1rem; font-size:1.05rem; font-weight:700; background:linear-gradient(135deg,var(--purple),var(--cyan)); border:none; border-radius:14px; color:#fff; cursor:pointer; position:relative; overflow:hidden; font-family:'DM Sans',sans-serif; transition:transform 0.2s; }
.btn-analyze:hover { transform:translateY(-2px); }
.loading-overlay { display:none; position:fixed; inset:0; background:rgba(0,0,0,0.7); backdrop-filter:blur(8px); z-index:200; align-items:center; justify-content:center; flex-direction:column; gap:1.5rem; }
.loading-overlay.show { display:flex; }
.spinner { width:60px; height:60px; border:3px solid rgba(124,58,237,0.3); border-top-color:var(--purple); border-radius:50%; animation:spin 0.8s linear infinite; }
@keyframes spin { to { transform:rotate(360deg); } }
.loading-text { font-family:'Syne',sans-serif; font-size:1.2rem; color:var(--text); }

/* RESULT PAGE */
#result { background:var(--dark); padding-top:80px; min-height:100vh; }
.result-container { max-width:1100px; margin:0 auto; padding:4rem 2rem; }
.result-header { text-align:center; margin-bottom:3rem; }
.score-ring { width:180px; height:180px; margin:0 auto 2rem; position:relative; }
.score-ring svg { transform:rotate(-90deg); }
.score-text { position:absolute; inset:0; display:flex; flex-direction:column; align-items:center; justify-content:center; }
.score-num { font-family:'Syne',sans-serif; font-size:2.5rem; font-weight:800; }
.score-label { font-size:0.8rem; color:var(--text-muted); margin-top:2px; }
.risk-badge { display:inline-flex; align-items:center; gap:8px; padding:8px 20px; border-radius:50px; font-weight:700; font-size:0.9rem; margin-bottom:1.5rem; }
.risk-safe { background:rgba(16,185,129,0.15); border:1px solid rgba(16,185,129,0.4); color:#10b981; }
.risk-suspicious { background:rgba(245,158,11,0.15); border:1px solid rgba(245,158,11,0.4); color:#f59e0b; }
.risk-high { background:rgba(239,68,68,0.15); border:1px solid rgba(239,68,68,0.4); color:#ef4444; }
.result-grid { display:grid; grid-template-columns:2fr 1fr; gap:2rem; margin-top:2rem; }
.reasons-card { background:var(--glass); border:1px solid var(--border); border-radius:20px; padding:2rem; }
.reasons-card h3 { font-family:'Syne',sans-serif; font-size:1.1rem; margin-bottom:1.5rem; }
.reason-item { display:flex; align-items:flex-start; gap:12px; padding:1rem; background:rgba(239,68,68,0.06); border:1px solid rgba(239,68,68,0.15); border-radius:12px; margin-bottom:0.75rem; }
.reason-icon { font-size:1.2rem; flex-shrink:0; }
.reason-text { font-size:0.9rem; line-height:1.5; }
.reason-score { font-size:0.75rem; color:var(--red); font-weight:600; margin-top:4px; }
.safe-item { background:rgba(16,185,129,0.06); border-color:rgba(16,185,129,0.15); }
.keyword-list { display:flex; flex-wrap:wrap; gap:8px; margin-top:1rem; }
.keyword-tag { background:rgba(239,68,68,0.15); border:1px solid rgba(239,68,68,0.3); color:#fca5a5; padding:4px 12px; border-radius:50px; font-size:0.8rem; }
.safe-tag { background:rgba(16,185,129,0.15); border-color:rgba(16,185,129,0.3); color:#6ee7b7; }
.charts-row { display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; margin-top:2rem; }
.chart-card { background:var(--glass); border:1px solid var(--border); border-radius:20px; padding:1.75rem; }
.chart-card h3 { font-family:'Syne',sans-serif; font-size:1rem; margin-bottom:1.25rem; }
.recommendation { background:linear-gradient(135deg,rgba(6,182,212,0.1),rgba(124,58,237,0.1)); border:1px solid rgba(124,58,237,0.3); border-radius:20px; padding:2rem; margin-top:2rem; }
.rec-title { font-family:'Syne',sans-serif; font-size:1.1rem; margin-bottom:1rem; }
.rec-list { display:flex; flex-direction:column; gap:8px; }
.rec-item { display:flex; gap:10px; font-size:0.9rem; color:var(--text-muted); }
.rec-bullet { color:var(--cyan); font-weight:700; flex-shrink:0; }
.side-panel { display:flex; flex-direction:column; gap:1.5rem; }
.side-card { background:var(--glass); border:1px solid var(--border); border-radius:20px; padding:1.75rem; }
.side-card h3 { font-family:'Syne',sans-serif; font-size:1rem; margin-bottom:1.25rem; }
.trust-item { display:flex; align-items:center; gap:10px; padding:0.6rem 0; border-bottom:1px solid var(--border); font-size:0.9rem; }
.trust-item:last-child { border-bottom:none; }
.trust-icon { width:28px; height:28px; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:0.85rem; flex-shrink:0; }
.trust-ok { background:rgba(16,185,129,0.15); }
.trust-warn { background:rgba(239,68,68,0.15); }
.pdf-btn { width:100%; background:linear-gradient(135deg,var(--blue-dark),var(--purple)); border:none; color:#fff; padding:0.85rem; border-radius:12px; font-family:'DM Sans',sans-serif; font-size:0.9rem; font-weight:600; cursor:pointer; transition:transform 0.2s; }
.pdf-btn:hover { transform:translateY(-2px); }

/* ADMIN DASHBOARD */
#admin { background:var(--dark); padding-top:80px; min-height:100vh; }
.admin-layout { display:grid; grid-template-columns:240px 1fr; min-height:calc(100vh - 64px); }
.sidebar { background:var(--dark2); border-right:1px solid var(--border); padding:1.5rem 0; position:sticky; top:64px; height:calc(100vh - 64px); overflow-y:auto; }
.sidebar-logo { padding:0 1.5rem 1.5rem; border-bottom:1px solid var(--border); margin-bottom:1rem; font-family:'Syne',sans-serif; font-size:0.85rem; font-weight:700; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.1em; }
.sidebar-item { display:flex; align-items:center; gap:10px; padding:0.75rem 1.5rem; font-size:0.9rem; color:var(--text-muted); cursor:pointer; transition:all 0.2s; border-left:3px solid transparent; }
.sidebar-item:hover { color:var(--text); background:rgba(255,255,255,0.04); }
.sidebar-item.active { color:var(--purple-light); border-left-color:var(--purple); background:rgba(124,58,237,0.1); }
.sidebar-item span { font-size:1rem; }
.dash-content { padding:2.5rem; overflow-y:auto; }
.dash-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:2rem; }
.dash-header h2 { font-family:'Syne',sans-serif; font-size:1.5rem; font-weight:700; }
.date-badge { font-size:0.8rem; color:var(--text-muted); background:var(--glass); border:1px solid var(--border); padding:6px 14px; border-radius:8px; }
.metrics-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:1.25rem; margin-bottom:2rem; }
.metric-card { border-radius:16px; padding:1.5rem; position:relative; overflow:hidden; }
.metric-card::after { content:''; position:absolute; right:-20px; bottom:-20px; width:80px; height:80px; border-radius:50%; opacity:0.2; }
.metric-val { font-family:'Syne',sans-serif; font-size:2rem; font-weight:800; margin-bottom:4px; }
.metric-lbl { font-size:0.8rem; opacity:0.7; }
.metric-change { font-size:0.75rem; margin-top:8px; display:flex; align-items:center; gap:4px; }
.metric-up { color:#10b981; }
.metric-down { color:#ef4444; }
.mc1 { background:linear-gradient(135deg,#4c1d95,#7c3aed); color:#fff; }
.mc1::after { background:#a78bfa; }
.mc2 { background:linear-gradient(135deg,#991b1b,#dc2626); color:#fff; }
.mc2::after { background:#f87171; }
.mc3 { background:linear-gradient(135deg,#065f46,#059669); color:#fff; }
.mc3::after { background:#6ee7b7; }
.mc4 { background:linear-gradient(135deg,#1e3a8a,#2563eb); color:#fff; }
.mc4::after { background:#93c5fd; }
.dash-row { display:grid; grid-template-columns:3fr 2fr; gap:1.5rem; margin-bottom:1.5rem; }
.dash-card { background:var(--glass); border:1px solid var(--border); border-radius:20px; padding:1.75rem; }
.dash-card-title { font-family:'Syne',sans-serif; font-size:1rem; font-weight:700; margin-bottom:1.5rem; display:flex; justify-content:space-between; align-items:center; }
.dash-card-title span { font-family:'DM Sans',sans-serif; font-size:0.75rem; font-weight:400; color:var(--text-muted); }
.keywords-list { display:flex; flex-direction:column; gap:10px; }
.kw-item { display:flex; align-items:center; gap:12px; }
.kw-bar-bg { flex:1; background:rgba(255,255,255,0.06); border-radius:50px; height:6px; overflow:hidden; }
.kw-bar { height:100%; border-radius:50px; background:linear-gradient(90deg,var(--purple),var(--pink)); }
.kw-label { font-size:0.8rem; width:160px; color:var(--text-muted); }
.kw-count { font-size:0.8rem; font-weight:600; width:30px; text-align:right; }
.table-search { display:flex; gap:1rem; margin-bottom:1.25rem; align-items:center; }
.table-search input { flex:1; }
.filter-select { background:rgba(255,255,255,0.06); border:1px solid var(--border); border-radius:10px; padding:0.6rem 1rem; color:var(--text); font-family:'DM Sans',sans-serif; font-size:0.85rem; }
.data-table { width:100%; border-collapse:collapse; font-size:0.85rem; }
.data-table th { padding:10px 14px; text-align:left; color:var(--text-muted); font-weight:500; border-bottom:1px solid var(--border); white-space:nowrap; }
.data-table td { padding:12px 14px; border-bottom:1px solid rgba(255,255,255,0.05); }
.data-table tr:hover td { background:rgba(255,255,255,0.02); }
.badge { display:inline-flex; padding:3px 10px; border-radius:50px; font-size:0.75rem; font-weight:600; }
.badge-safe { background:rgba(16,185,129,0.15); color:#10b981; }
.badge-suspicious { background:rgba(245,158,11,0.15); color:#f59e0b; }
.badge-high { background:rgba(239,68,68,0.15); color:#ef4444; }
.score-pill { display:inline-flex; align-items:center; gap:4px; font-weight:700; }
.trend-chart-wrap { height:200px; position:relative; }
.pie-wrap { height:200px; position:relative; }
.heatmap-grid { display:grid; grid-template-columns:repeat(7,1fr); gap:4px; margin-top:0.5rem; }
.hm-cell { height:28px; border-radius:4px; transition:opacity 0.2s; cursor:default; }
.hm-cell:hover { opacity:0.8; }
.hm-labels { display:grid; grid-template-columns:repeat(7,1fr); gap:4px; margin-bottom:4px; }
.hm-label { font-size:0.65rem; color:var(--text-muted); text-align:center; }
.export-btn { background:var(--glass); border:1px solid var(--border); border-radius:10px; padding:0.55rem 1.1rem; color:var(--text); font-family:'DM Sans',sans-serif; font-size:0.85rem; cursor:pointer; display:flex; align-items:center; gap:6px; transition:all 0.2s; }
.export-btn:hover { border-color:var(--purple-light); background:rgba(124,58,237,0.1); }

/* TOAST */
.toast-container { position:fixed; bottom:2rem; right:2rem; z-index:500; display:flex; flex-direction:column; gap:10px; }
.toast { background:var(--dark2); border:1px solid var(--border); border-radius:12px; padding:1rem 1.25rem; display:flex; align-items:center; gap:12px; min-width:260px; animation:slideIn 0.3s ease; box-shadow:0 10px 40px rgba(0,0,0,0.4); }
@keyframes slideIn { from{opacity:0;transform:translateX(20px)} to{opacity:1;transform:translateX(0)} }
.toast-icon { font-size:1.2rem; }
.toast-text { font-size:0.9rem; }
.toast-success { border-color:rgba(16,185,129,0.4); }
.toast-error { border-color:rgba(239,68,68,0.4); }
.toast-info { border-color:rgba(6,182,212,0.4); }

/* PROGRESS */
.progress-section { margin-top:1.5rem; }
.progress-item { margin-bottom:1rem; }
.progress-header { display:flex; justify-content:space-between; font-size:0.85rem; margin-bottom:6px; }
.progress-label { color:var(--text-muted); }
.progress-val { font-weight:600; }
.progress-bg { background:rgba(255,255,255,0.06); border-radius:50px; height:8px; overflow:hidden; }
.progress-fill { height:100%; border-radius:50px; animation:growBar 1.2s cubic-bezier(0.34,1.56,0.64,1) forwards; }
@keyframes growBar { from{width:0} }

/* RESPONSIVE */
@media(max-width:900px) {
  .features-grid, .testimonials-grid, .scam-grid, .result-grid, .dash-row { grid-template-columns:1fr; }
  .stats-strip { grid-template-columns:repeat(2,1fr); margin:0 1rem; }
  .metrics-grid { grid-template-columns:repeat(2,1fr); }
  .admin-layout { grid-template-columns:1fr; }
  .sidebar { display:none; }
  .form-grid { grid-template-columns:1fr; }
  .charts-row { grid-template-columns:1fr; }
  .section, .scam-section, footer { padding-left:1.5rem; padding-right:1.5rem; }
  .hero { padding:120px 1.5rem 60px; }
}
</style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="logo">🛡️ InternShield</div>
  <div class="nav-links">
    <a onclick="showPage('landing')" class="active" id="nav-landing">Home</a>
    <a onclick="showPage('analysis')" id="nav-analysis">Check Internship</a>
    <a onclick="showPage('admin')" id="nav-admin">Dashboard</a>
    <button class="btn-nav btn-primary" onclick="showPage('analysis')">Analyze Now →</button>
  </div>
</nav>

<!-- LANDING PAGE -->
<div id="landing" class="page active">
  <div class="hero">
    <div class="hero-badge"><span></span> AI-Powered Scam Detection Platform</div>
    <h1 class="hero-title">Don't Fall for <span class="grad-text">Fake Internships</span>. Detect Them First.</h1>
    <p>InternShield uses advanced rule-based analytics to analyze internship offers and reveal red flags — before you lose money or time.</p>
    <div class="hero-btns">
      <button class="btn-primary" onclick="showPage('analysis')">🔍 Analyze an Internship</button>
      <button class="btn-outline" onclick="showPage('admin')">📊 View Analytics</button>
    </div>
  </div>

  <div class="stats-strip">
    <div class="stat-item"><div class="stat-num" id="cnt1">0</div><div class="stat-label">Internships Analyzed</div></div>
    <div class="stat-item"><div class="stat-num" id="cnt2">0%</div><div class="stat-label">Fake Detection Rate</div></div>
    <div class="stat-item"><div class="stat-num" id="cnt3">0</div><div class="stat-label">Students Protected</div></div>
    <div class="stat-item"><div class="stat-num" id="cnt4">0</div><div class="stat-label">Scam Patterns Tracked</div></div>
  </div>

  <div class="section">
    <div class="section-label">Core Features</div>
    <div class="section-title">Everything You Need to <span class="grad-text">Stay Safe</span></div>
    <div class="section-sub">Our platform gives students the tools to identify suspicious internship offers before they cause harm.</div>
    <div class="features-grid">
      <div class="feature-card" style="--glow-start:rgba(124,58,237,0.1)">
        <div class="feature-icon" style="background:rgba(124,58,237,0.2)">🎯</div>
        <h3>Risk Scoring Engine</h3>
        <p>Rule-based analytics evaluate 7+ risk factors and generate a 0–100 scam risk score in seconds.</p>
      </div>
      <div class="feature-card" style="--glow-start:rgba(6,182,212,0.1)">
        <div class="feature-icon" style="background:rgba(6,182,212,0.2)">🔑</div>
        <h3>Keyword Detection</h3>
        <p>Automatically flags scam-associated phrases like "guaranteed placement", "pay now", and "100% job guarantee".</p>
      </div>
      <div class="feature-card" style="--glow-start:rgba(236,72,153,0.1)">
        <div class="feature-icon" style="background:rgba(236,72,153,0.2)">📊</div>
        <h3>Visual Analytics</h3>
        <p>Charts and graphs break down exactly why an internship was flagged, with color-coded indicators.</p>
      </div>
      <div class="feature-card" style="--glow-start:rgba(16,185,129,0.1)">
        <div class="feature-icon" style="background:rgba(16,185,129,0.2)">🛡️</div>
        <h3>Trust Indicators</h3>
        <p>Positive signals like official domains, transparent salary, and interview processes boost trust score.</p>
      </div>
      <div class="feature-card" style="--glow-start:rgba(245,158,11,0.1)">
        <div class="feature-icon" style="background:rgba(245,158,11,0.2)">📄</div>
        <h3>PDF Export</h3>
        <p>Download a full risk analysis report to share with friends, parents, or college placement cells.</p>
      </div>
      <div class="feature-card" style="--glow-start:rgba(59,130,246,0.1)">
        <div class="feature-icon" style="background:rgba(59,130,246,0.2)">📈</div>
        <h3>Admin Dashboard</h3>
        <p>Track trends, common scam keywords, and submission history with an analytics-grade admin view.</p>
      </div>
    </div>
  </div>

  <div class="scam-section" style="max-width:1100px;margin:0 auto 4rem;margin-left:4rem;margin-right:4rem;">
    <div class="section-label" style="color:var(--red)">⚠️ Scam Awareness</div>
    <div class="section-title">Common Red Flags to Watch For</div>
    <div class="scam-grid">
      <div class="scam-item"><div class="scam-dot"></div><p><strong>Registration / Processing Fees:</strong> Legitimate companies never ask students to pay a fee to join an internship program.</p></div>
      <div class="scam-item"><div class="scam-dot"></div><p><strong>Gmail / Yahoo Email IDs:</strong> Real companies use official business domain emails, not free providers.</p></div>
      <div class="scam-item"><div class="scam-dot"></div><p><strong>Guaranteed Placement Promises:</strong> No ethical company can guarantee 100% placement — it's a classic lure.</p></div>
      <div class="scam-item"><div class="scam-dot"></div><p><strong>No Official Website:</strong> Reputable organizations have verified web presence. No website = high risk.</p></div>
      <div class="scam-item"><div class="scam-dot"></div><p><strong>WhatsApp-Only Communication:</strong> Scammers avoid traceable official channels and prefer informal apps.</p></div>
      <div class="scam-item"><div class="scam-dot"></div><p><strong>Unrealistic Salary for Interns:</strong> ₹50,000+/month for a beginner internship with no experience? Big red flag.</p></div>
    </div>
  </div>

  <div class="section">
    <div class="section-label">Testimonials</div>
    <div class="section-title">Students Who <span class="grad-text">Stayed Safe</span></div>
    <div class="testimonials-grid">
      <div class="testimonial-card">
        <div class="stars">★★★★★</div>
        <p>"I almost paid ₹2,000 for a 'training kit' before InternShield flagged it as 92% fake. Saved my money and time!"</p>
        <div class="t-author"><div class="t-avatar" style="background:rgba(124,58,237,0.3);color:var(--purple-light)">AP</div><div><div class="t-name">Arjun Patel</div><div class="t-role">CS Student, BITS Pilani</div></div></div>
      </div>
      <div class="testimonial-card">
        <div class="stars">★★★★★</div>
        <p>"The keyword detection caught 'instant certificate' and 'no interview needed' in the description immediately. Super accurate!"</p>
        <div class="t-author"><div class="t-avatar" style="background:rgba(6,182,212,0.2);color:var(--cyan)">SR</div><div><div class="t-name">Sneha Rao</div><div class="t-role">MBA Student, IIM Indore</div></div></div>
      </div>
      <div class="testimonial-card">
        <div class="stars">★★★★☆</div>
        <p>"Our college placement cell uses InternShield to vet internships before posting them on the board. An essential tool!"</p>
        <div class="t-author"><div class="t-avatar" style="background:rgba(236,72,153,0.2);color:var(--pink)">DK</div><div><div class="t-name">Dr. Deepa Kumar</div><div class="t-role">Placement Officer, VIT</div></div></div>
      </div>
    </div>
  </div>

  <footer>
    <div class="foot-logo">🛡️ InternShield</div>
    <p>Protecting students from fake internship scams with data-driven analytics.</p>
    <p style="margin-top:1rem;font-size:0.75rem;">Built with Laravel 11 · MySQL · Tailwind CSS · Chart.js &nbsp;|&nbsp; © 2025 InternShield</p>
  </footer>
</div>

<!-- ANALYSIS FORM PAGE -->
<div id="analysis" class="page">
  <div class="form-container">
    <div class="form-header">
      <div class="section-label" style="color:var(--cyan)">🔍 Risk Analysis</div>
      <h2 class="section-title">Check Your Internship Offer</h2>
      <p style="color:var(--text-muted);max-width:500px;margin:0 auto;font-size:0.95rem">Fill in the details below. Our engine will analyze 7+ risk factors and give you an instant scam risk score.</p>
    </div>
    <div class="form-card">
      <div class="form-grid">
        <div class="form-group">
          <label>Company Name *</label>
          <input type="text" id="f_company" placeholder="e.g. Infosys, XYZ Solutions" oninput="updateLiveRisk()">
        </div>
        <div class="form-group">
          <label>Internship Role *</label>
          <input type="text" id="f_role" placeholder="e.g. Web Developer, Marketing Intern">
        </div>
        <div class="form-group">
          <label>Contact Email *</label>
          <input type="email" id="f_email" placeholder="contact@company.com" oninput="updateLiveRisk()">
        </div>
        <div class="form-group">
          <label>Website URL</label>
          <input type="text" id="f_website" placeholder="https://www.company.com" oninput="updateLiveRisk()">
        </div>
        <div class="form-group">
          <label>Registration / Processing Fee (₹)</label>
          <input type="number" id="f_fee" placeholder="0 (enter 0 if no fee)" oninput="updateLiveRisk()" min="0">
        </div>
        <div class="form-group">
          <label>Monthly Salary Offered (₹)</label>
          <input type="number" id="f_salary" placeholder="e.g. 10000" oninput="updateLiveRisk()" min="0">
        </div>
        <div class="form-group">
          <label>Primary Communication Method</label>
          <select id="f_comm" onchange="updateLiveRisk()">
            <option value="">Select method</option>
            <option value="whatsapp">WhatsApp Only</option>
            <option value="email">Official Email</option>
            <option value="phone">Phone + Email</option>
            <option value="portal">Company Portal</option>
          </select>
        </div>
        <div class="form-group">
          <label>Certificate Guaranteed?</label>
          <select id="f_cert" onchange="updateLiveRisk()">
            <option value="">Select</option>
            <option value="yes_guaranteed">Yes – Guaranteed Instantly</option>
            <option value="yes_after">Yes – After Completion</option>
            <option value="no">No Certificate Mentioned</option>
          </select>
        </div>
        <div class="form-group full">
          <label>Internship Description *</label>
          <textarea id="f_desc" placeholder="Paste the full internship offer description here..." oninput="updateLiveRisk()" rows="5"></textarea>
        </div>
      </div>

      <div class="risk-meter-preview">
        <div class="risk-meter-label">Live Risk Preview — <span id="live-risk-label" style="color:var(--green);font-weight:600">Low Risk</span></div>
        <div class="risk-bar-bg"><div class="risk-bar-fill" id="live-risk-bar"></div></div>
        <div style="display:flex;justify-content:space-between;font-size:0.7rem;color:var(--text-muted);margin-top:6px"><span>Safe (0)</span><span>Suspicious (40–70)</span><span>High Risk (100)</span></div>
      </div>

      <button class="btn-analyze" onclick="runAnalysis()">🔍 Analyze Internship Risk</button>
    </div>
  </div>
</div>

<!-- RESULT PAGE -->
<div id="result" class="page">
  <div class="result-container">
    <div class="result-header">
      <div id="result-score-ring" class="score-ring">
        <svg width="180" height="180" viewBox="0 0 180 180">
          <circle cx="90" cy="90" r="75" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="14"/>
          <circle id="score-arc" cx="90" cy="90" r="75" fill="none" stroke="url(#scoreGrad)" stroke-width="14" stroke-linecap="round" stroke-dasharray="471" stroke-dashoffset="471"/>
          <defs>
            <linearGradient id="scoreGrad" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#10b981"/>
              <stop offset="50%" stop-color="#f59e0b"/>
              <stop offset="100%" stop-color="#ef4444"/>
            </linearGradient>
          </defs>
        </svg>
        <div class="score-text">
          <div class="score-num" id="result-score-num">0%</div>
          <div class="score-label">Risk Score</div>
        </div>
      </div>
      <div id="result-badge" class="risk-badge risk-safe">✅ SAFE</div>
      <div id="result-company-name" style="font-family:'Syne',sans-serif;font-size:1.2rem;margin-bottom:0.5rem"></div>
      <div id="result-role" style="color:var(--text-muted);font-size:0.9rem"></div>
    </div>

    <div class="result-grid">
      <div>
        <div class="reasons-card">
          <h3>🚩 Risk Factors Detected</h3>
          <div id="risk-reasons"></div>
        </div>
        <div class="reasons-card" style="margin-top:1.5rem">
          <h3>🔍 Scam Keywords Detected</h3>
          <div id="scam-keywords-found" class="keyword-list"></div>
          <h3 style="margin-top:1.25rem">✅ Trust Indicators Found</h3>
          <div id="safe-keywords-found" class="keyword-list"></div>
        </div>
        <div class="charts-row">
          <div class="chart-card">
            <h3>Risk Distribution</h3>
            <div class="pie-wrap"><canvas id="resultPieChart" role="img" aria-label="Pie chart showing risk score vs safe score distribution"></canvas></div>
          </div>
          <div class="chart-card">
            <h3>Scam Pattern Scores</h3>
            <div style="height:200px;position:relative"><canvas id="resultBarChart" role="img" aria-label="Bar chart of scam pattern scores detected in the internship"></canvas></div>
          </div>
        </div>
        <div class="recommendation" id="recommendations">
          <div class="rec-title">📋 Our Recommendations</div>
          <div class="rec-list" id="rec-list"></div>
        </div>
      </div>
      <div class="side-panel">
        <div class="side-card">
          <h3>🔎 Trust Checklist</h3>
          <div id="trust-checklist"></div>
        </div>
        <div class="side-card">
          <h3>📊 Risk Breakdown</h3>
          <div class="progress-section" id="risk-breakdown"></div>
        </div>
        <button class="pdf-btn" onclick="exportPDF()">📄 Export as PDF Report</button>
        <button class="btn-outline" style="width:100%;margin-top:0.5rem" onclick="showPage('analysis')">← Analyze Another</button>
      </div>
    </div>
  </div>
</div>

<!-- ADMIN DASHBOARD -->
<div id="admin" class="page">
  <div class="admin-layout">
    <div class="sidebar">
      <div class="sidebar-logo">Analytics</div>
      <div class="sidebar-item active" onclick="setDashSection(this,'overview')"><span>📊</span> Overview</div>
      <div class="sidebar-item" onclick="setDashSection(this,'submissions')"><span>📋</span> Submissions</div>
      <div class="sidebar-item" onclick="setDashSection(this,'trends')"><span>📈</span> Trends</div>
      <div class="sidebar-item" onclick="setDashSection(this,'keywords')"><span>🔑</span> Keywords</div>
      <div class="sidebar-item" onclick="showPage('analysis')"><span>🔍</span> New Analysis</div>
      <div style="padding:1rem 1.5rem;border-top:1px solid var(--border);margin-top:auto">
        <div style="font-size:0.75rem;color:var(--text-muted)">InternShield v2.0</div>
        <div style="font-size:0.7rem;color:var(--text-muted);margin-top:2px">Laravel 11 · MySQL</div>
      </div>
    </div>
    <div class="dash-content">
      <div class="dash-header">
        <div>
          <h2>Admin Analytics Dashboard</h2>
          <div style="font-size:0.85rem;color:var(--text-muted);margin-top:4px">Real-time internship scam intelligence</div>
        </div>
        <div style="display:flex;gap:10px;align-items:center">
          <div class="date-badge">📅 Today: <span id="today-date"></span></div>
          <button class="export-btn" onclick="showToast('📊 Analytics report downloaded!','success')">⬇ Export Report</button>
        </div>
      </div>

      <div class="metrics-grid">
        <div class="metric-card mc1">
          <div class="metric-val" id="m1">0</div>
          <div class="metric-lbl">Total Analyzed</div>
          <div class="metric-change metric-up">▲ 12% this week</div>
        </div>
        <div class="metric-card mc2">
          <div class="metric-val" id="m2">0%</div>
          <div class="metric-lbl">Fake Rate</div>
          <div class="metric-change metric-down">▲ 5% from last week</div>
        </div>
        <div class="metric-card mc3">
          <div class="metric-val" id="m3">0%</div>
          <div class="metric-lbl">Genuine Rate</div>
          <div class="metric-change metric-up">▼ 3% from last week</div>
        </div>
        <div class="metric-card mc4">
          <div class="metric-val" id="m4">0</div>
          <div class="metric-lbl">Avg Risk Score</div>
          <div class="metric-change">Stable this week</div>
        </div>
      </div>

      <div class="dash-row">
        <div class="dash-card">
          <div class="dash-card-title">Weekly Submission Trend <span>Last 7 days</span></div>
          <div class="trend-chart-wrap"><canvas id="trendChart" role="img" aria-label="Line chart showing weekly internship submission trends"></canvas></div>
        </div>
        <div class="dash-card">
          <div class="dash-card-title">Risk Distribution <span>All submissions</span></div>
          <div class="pie-wrap"><canvas id="adminPieChart" role="img" aria-label="Doughnut chart showing safe, suspicious and high risk distribution"></canvas></div>
        </div>
      </div>

      <div class="dash-row">
        <div class="dash-card">
          <div class="dash-card-title">Top Scam Keywords <span>Frequency count</span></div>
          <div class="keywords-list" id="kw-list"></div>
        </div>
        <div class="dash-card">
          <div class="dash-card-title">Activity Heatmap <span>Submissions by day</span></div>
          <div class="hm-labels"><div class="hm-label">M</div><div class="hm-label">T</div><div class="hm-label">W</div><div class="hm-label">T</div><div class="hm-label">F</div><div class="hm-label">S</div><div class="hm-label">S</div></div>
          <div class="heatmap-grid" id="heatmap"></div>
        </div>
      </div>

      <div class="dash-card">
        <div class="dash-card-title">Recent Submissions <span>Latest 20 entries</span></div>
        <div class="table-search">
          <input type="text" placeholder="Search by company or role..." oninput="filterTable(this.value)" style="max-width:320px">
          <select class="filter-select" onchange="filterByRisk(this.value)">
            <option value="all">All Risk Levels</option>
            <option value="safe">Safe</option>
            <option value="suspicious">Suspicious</option>
            <option value="high">High Risk</option>
          </select>
        </div>
        <div style="overflow-x:auto">
          <table class="data-table" id="submissions-table">
            <thead><tr><th>#</th><th>Company</th><th>Role</th><th>Score</th><th>Risk Level</th><th>Fee</th><th>Submitted</th></tr></thead>
            <tbody id="table-body"></tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- LOADING OVERLAY -->
<div class="loading-overlay" id="loading">
  <div class="spinner"></div>
  <div class="loading-text">Analyzing Risk Factors...</div>
  <div style="color:var(--text-muted);font-size:0.9rem">Checking 7+ indicators</div>
</div>

<!-- TOAST CONTAINER -->
<div class="toast-container" id="toasts"></div>

<script>
// ─── SAMPLE DATA ───────────────────────────────────────────────
const sampleData = [
  {company:"TechStar India",role:"Web Developer Intern",score:15,risk:"safe",fee:0,date:"2025-05-20"},
  {company:"FakePlacements.in",role:"HR Trainee",score:92,risk:"high",fee:2000,date:"2025-05-19"},
  {company:"Google India",role:"SWE Intern",score:8,risk:"safe",fee:0,date:"2025-05-19"},
  {company:"EasyJobs247",role:"Marketing Intern",score:78,risk:"high",fee:1500,date:"2025-05-18"},
  {company:"Infosys BPO",role:"Data Analyst Intern",score:12,risk:"safe",fee:0,date:"2025-05-18"},
  {company:"QuickCert Solutions",role:"Digital Marketing",score:85,risk:"high",fee:999,date:"2025-05-17"},
  {company:"Amazon Dev",role:"Cloud Intern",score:10,risk:"safe",fee:0,date:"2025-05-17"},
  {company:"InstaCertify",role:"Content Writer",score:55,risk:"suspicious",fee:500,date:"2025-05-16"},
  {company:"Microsoft IDC",role:"ML Research Intern",score:5,risk:"safe",fee:0,date:"2025-05-16"},
  {company:"JobGuarantee.co",role:"Sales Intern",score:95,risk:"high",fee:3000,date:"2025-05-15"},
  {company:"Wipro Technologies",role:"Testing Intern",score:18,risk:"safe",fee:0,date:"2025-05-15"},
  {company:"PayNow Training",role:"Java Developer",score:88,risk:"high",fee:1200,date:"2025-05-14"},
  {company:"Zomato",role:"Product Intern",score:20,risk:"safe",fee:0,date:"2025-05-14"},
  {company:"UrgentHire India",role:"HR Executive",score:45,risk:"suspicious",fee:0,date:"2025-05-13"},
  {company:"Flipkart",role:"UI/UX Intern",score:14,risk:"safe",fee:0,date:"2025-05-13"},
  {company:"100JobsGuaranteed",role:"Business Dev",score:98,risk:"high",fee:5000,date:"2025-05-12"},
  {company:"Razorpay",role:"Finance Intern",score:11,risk:"safe",fee:0,date:"2025-05-12"},
  {company:"WhatsAppJobs",role:"Social Media Mgr",score:62,risk:"suspicious",fee:0,date:"2025-05-11"},
  {company:"TATA Consultancy",role:"SAP Intern",score:9,risk:"safe",fee:0,date:"2025-05-11"},
  {company:"EarnEasy Solutions",role:"Data Entry Intern",score:72,risk:"high",fee:800,date:"2025-05-10"},
];

const keywords_freq = [
  {kw:"guaranteed placement",count:47},
  {kw:"pay now",count:38},
  {kw:"instant certificate",count:31},
  {kw:"limited seats",count:28},
  {kw:"100% job guarantee",count:25},
  {kw:"no interview",count:20},
  {kw:"urgent payment",count:15},
];

// ─── PAGE ROUTING ──────────────────────────────────────────────
let resultPieChartInst, resultBarChartInst, trendChartInst, adminPieChartInst;

function showPage(id) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  const navEl = document.getElementById('nav-'+id);
  if(navEl) navEl.classList.add('active');
  window.scrollTo(0,0);
  if(id==='admin') initDashboard();
  if(id==='landing') animateCounters();
}

// ─── COUNTERS ──────────────────────────────────────────────────
function animateCounters() {
  animCount('cnt1',2847,0,'');
  setTimeout(()=>animCount('cnt2',73,0,'%'),200);
  setTimeout(()=>animCount('cnt3',1250,0,''),400);
  setTimeout(()=>animCount('cnt4',127,0,''),600);
}
function animCount(id,target,current,suffix) {
  const el=document.getElementById(id);
  const step=Math.ceil(target/60);
  const timer=setInterval(()=>{
    current=Math.min(current+step,target);
    el.textContent=current.toLocaleString()+suffix;
    if(current>=target) clearInterval(timer);
  },20);
}

// ─── LIVE RISK PREVIEW ─────────────────────────────────────────
function updateLiveRisk() {
  const score = calcScore();
  const pct = Math.min(score, 100);
  document.getElementById('live-risk-bar').style.width = pct + '%';
  const lbl = document.getElementById('live-risk-label');
  if(pct < 40) { lbl.textContent = 'Low Risk'; lbl.style.color = 'var(--green)'; }
  else if(pct < 70) { lbl.textContent = 'Suspicious'; lbl.style.color = 'var(--amber)'; }
  else { lbl.textContent = 'High Risk'; lbl.style.color = 'var(--red)'; }
}

function calcScore() {
  let score = 0;
  const fee = parseFloat(document.getElementById('f_fee').value) || 0;
  const email = (document.getElementById('f_email').value || '').toLowerCase();
  const website = (document.getElementById('f_website').value || '').toLowerCase();
  const salary = parseFloat(document.getElementById('f_salary').value) || 0;
  const comm = document.getElementById('f_comm').value;
  const cert = document.getElementById('f_cert').value;
  const desc = (document.getElementById('f_desc').value || '').toLowerCase();

  if(fee > 0) score += 30;
  if(email.includes('@gmail') || email.includes('@yahoo') || email.includes('@hotmail')) score += 20;
  if(!website || website.length < 5) score += 25;
  if(salary > 50000) score += 15;
  if(comm === 'whatsapp') score += 10;
  if(cert === 'yes_guaranteed') score += 15;

  const scamKws = ['guaranteed placement','instant certificate','pay now','limited seats','no interview','100% job guarantee','urgent payment','easy earnings','work from home earn','unlimited income'];
  let kwCount = 0;
  scamKws.forEach(kw => { if(desc.includes(kw)) kwCount++; });
  score += kwCount * 10;
  return Math.min(score, 100);
}

// ─── ANALYSIS ─────────────────────────────────────────────────
function runAnalysis() {
  const company = document.getElementById('f_company').value.trim();
  const role = document.getElementById('f_role').value.trim();
  if(!company || !role) { showToast('Please fill Company Name and Role','error'); return; }
  document.getElementById('loading').classList.add('show');
  setTimeout(() => {
    document.getElementById('loading').classList.remove('show');
    buildResult();
    showPage('result');
    showToast('Analysis complete!','success');
  }, 2200);
}

function buildResult() {
  const company = document.getElementById('f_company').value.trim();
  const role = document.getElementById('f_role').value.trim();
  const fee = parseFloat(document.getElementById('f_fee').value) || 0;
  const email = (document.getElementById('f_email').value || '').toLowerCase();
  const website = (document.getElementById('f_website').value || '').toLowerCase();
  const salary = parseFloat(document.getElementById('f_salary').value) || 0;
  const comm = document.getElementById('f_comm').value;
  const cert = document.getElementById('f_cert').value;
  const desc = (document.getElementById('f_desc').value || '').toLowerCase();

  let score = 0;
  const reasons = [];
  const breakdown = [];

  if(fee > 0) {
    score += 30;
    reasons.push({icon:'💸', text:'Registration fee required (₹'+fee+')', score:30, bad:true});
    breakdown.push({label:'Registration Fee', val:30, color:'#ef4444'});
  }
  if(email.includes('@gmail') || email.includes('@yahoo') || email.includes('@hotmail')) {
    score += 20;
    reasons.push({icon:'📧', text:'Non-official email domain ('+email+')', score:20, bad:true});
    breakdown.push({label:'Email Domain', val:20, color:'#f97316'});
  }
  if(!website || website.length < 5) {
    score += 25;
    reasons.push({icon:'🌐', text:'No official website provided', score:25, bad:true});
    breakdown.push({label:'No Website', val:25, color:'#ef4444'});
  }
  if(salary > 50000) {
    score += 15;
    reasons.push({icon:'💰', text:'Unrealistically high salary offer (₹'+salary+'/mo)', score:15, bad:true});
    breakdown.push({label:'Unrealistic Salary', val:15, color:'#f59e0b'});
  }
  if(comm === 'whatsapp') {
    score += 10;
    reasons.push({icon:'📱', text:'WhatsApp-only communication channel', score:10, bad:true});
    breakdown.push({label:'WhatsApp Only', val:10, color:'#a78bfa'});
  }
  if(cert === 'yes_guaranteed') {
    score += 15;
    reasons.push({icon:'📜', text:'Instant certificate guaranteed — suspicious promise', score:15, bad:true});
    breakdown.push({label:'Instant Certificate', val:15, color:'#ec4899'});
  }

  const scamKws = ['guaranteed placement','instant certificate','pay now','limited seats','no interview','100% job guarantee','urgent payment','easy earnings','unlimited income'];
  const safeKws = ['technical interview','background check','official offer letter','tax deduction','pf/epf','nda agreement','probation period'];
  const foundScam = [], foundSafe = [];

  scamKws.forEach(kw => { if(desc.includes(kw)) { foundScam.push(kw); score += 10; } });
  safeKws.forEach(kw => { if(desc.includes(kw)) foundSafe.push(kw); });

  if(foundScam.length > 0) {
    reasons.push({icon:'🚫', text:foundScam.length+' scam keyword(s) detected in description', score:foundScam.length*10, bad:true});
    breakdown.push({label:'Scam Keywords', val:Math.min(foundScam.length*10,30), color:'#dc2626'});
  }
  if(comm === 'email' || comm === 'portal') {
    reasons.push({icon:'✅', text:'Uses official communication channel', score:-5, bad:false});
  }
  if(website && website.length > 5 && !email.includes('@gmail')) {
    reasons.push({icon:'🌐', text:'Official website and email domain present', score:-10, bad:false});
  }
  if(fee === 0 && salary > 0 && salary <= 50000) {
    reasons.push({icon:'💚', text:'No registration fee — positive sign', score:-5, bad:false});
  }

  score = Math.min(Math.max(score, 0), 100);

  // Update score ring
  const circumference = 471;
  const offset = circumference - (score / 100) * circumference;
  document.getElementById('score-arc').style.strokeDashoffset = offset;
  animateNumber('result-score-num', score, '%');

  // Risk badge
  const badge = document.getElementById('result-badge');
  badge.className = 'risk-badge';
  if(score < 40) { badge.classList.add('risk-safe'); badge.textContent = '✅ SAFE — Low Risk'; }
  else if(score < 70) { badge.classList.add('risk-suspicious'); badge.textContent = '⚠️ SUSPICIOUS — Medium Risk'; }
  else { badge.classList.add('risk-high'); badge.textContent = '🚨 HIGH RISK — Likely Scam'; }

  document.getElementById('result-company-name').textContent = company;
  document.getElementById('result-role').textContent = role;

  // Reasons
  const reasonsEl = document.getElementById('risk-reasons');
  reasonsEl.innerHTML = reasons.map(r => `
    <div class="reason-item ${r.bad?'':'safe-item'}">
      <span class="reason-icon">${r.icon}</span>
      <div><div class="reason-text">${r.text}</div>
      <div class="reason-score" style="color:${r.bad?'var(--red)':'var(--green)'}">${r.bad?'+':''}${r.score} points</div></div>
    </div>`).join('');

  // Keywords
  document.getElementById('scam-keywords-found').innerHTML = foundScam.length ? foundScam.map(k=>`<span class="keyword-tag">${k}</span>`).join('') : '<span style="color:var(--text-muted);font-size:0.85rem">No scam keywords found</span>';
  document.getElementById('safe-keywords-found').innerHTML = foundSafe.length ? foundSafe.map(k=>`<span class="keyword-tag safe-tag">${k}</span>`).join('') : '<span style="color:var(--text-muted);font-size:0.85rem">No trust keywords found</span>';

  // Trust checklist
  const checks = [
    {label:'Official email domain', ok: !(email.includes('@gmail')||email.includes('@yahoo')||email.includes('@hotmail'))},
    {label:'Has official website', ok: website && website.length>5},
    {label:'No registration fee', ok: fee===0},
    {label:'Realistic salary range', ok: salary<=50000 && salary>0},
    {label:'Official communication channel', ok: comm==='email'||comm==='portal'},
    {label:'No instant certificate promise', ok: cert!=='yes_guaranteed'},
    {label:'No scam keywords found', ok: foundScam.length===0},
  ];
  document.getElementById('trust-checklist').innerHTML = checks.map(c=>`
    <div class="trust-item">
      <div class="trust-icon ${c.ok?'trust-ok':'trust-warn'}">${c.ok?'✅':'❌'}</div>
      <div style="font-size:0.85rem;color:${c.ok?'var(--text)':'var(--text-muted)'}">${c.label}</div>
    </div>`).join('');

  // Risk breakdown progress bars
  document.getElementById('risk-breakdown').innerHTML = breakdown.map(b=>`
    <div class="progress-item">
      <div class="progress-header"><span class="progress-label">${b.label}</span><span class="progress-val" style="color:${b.color}">+${b.val}</span></div>
      <div class="progress-bg"><div class="progress-fill" style="width:${b.val*3}%;background:${b.color}"></div></div>
    </div>`).join('') || '<div style="color:var(--text-muted);font-size:0.85rem">No risk factors detected — looks safe!</div>';

  // Recommendations
  const recs = score >= 70 ? [
    'Do NOT pay any registration or processing fee under any circumstances.',
    'Verify the company on MCA (Ministry of Corporate Affairs) portal.',
    'Check Glassdoor and LinkedIn for company reviews.',
    'Report this to your placement cell or cybercrime portal.',
    'Contact the company via their official website (if exists) to verify.'
  ] : score >= 40 ? [
    'Proceed with caution — verify company details independently.',
    'Request an official offer letter before accepting.',
    'Speak with a placement officer for a second opinion.',
    'Confirm via LinkedIn that the recruiter is genuinely associated with the company.'
  ] : [
    'This offer appears legitimate based on our analysis.',
    'Always review the offer letter thoroughly before accepting.',
    'Confirm salary and role details in writing.',
    'Proceed with your application — the indicators look positive.'
  ];
  document.getElementById('rec-list').innerHTML = recs.map(r=>`<div class="rec-item"><span class="rec-bullet">→</span><span>${r}</span></div>`).join('');

  // Charts
  buildResultCharts(score, breakdown);
}

function animateNumber(id, target, suffix) {
  let cur = 0;
  const el = document.getElementById(id);
  const step = Math.ceil(target / 40);
  const t = setInterval(()=>{
    cur = Math.min(cur+step, target);
    el.textContent = cur + suffix;
    if(cur>=target) clearInterval(t);
  },30);
}

function buildResultCharts(score, breakdown) {
  if(resultPieChartInst) resultPieChartInst.destroy();
  if(resultBarChartInst) resultBarChartInst.destroy();

  const safe = 100 - score;
  resultPieChartInst = new Chart(document.getElementById('resultPieChart'), {
    type:'pie',
    data:{
      labels:['Risk Score','Safe Score'],
      datasets:[{data:[score,safe],backgroundColor:['#ef4444','#10b981'],borderWidth:0}]
    },
    options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}}}
  });

  if(breakdown.length > 0) {
    resultBarChartInst = new Chart(document.getElementById('resultBarChart'), {
      type:'bar',
      data:{
        labels: breakdown.map(b=>b.label),
        datasets:[{label:'Risk Points',data:breakdown.map(b=>b.val),backgroundColor:breakdown.map(b=>b.color+'cc'),borderRadius:6}]
      },
      options:{
        responsive:true,maintainAspectRatio:false,
        plugins:{legend:{display:false}},
        scales:{
          x:{ticks:{color:'#9d89c4',font:{size:10}},grid:{color:'rgba(255,255,255,0.05)'}},
          y:{ticks:{color:'#9d89c4'},grid:{color:'rgba(255,255,255,0.05)'}}
        }
      }
    });
  }
}

// ─── DASHBOARD ────────────────────────────────────────────────
let dashReady = false;
function initDashboard() {
  if(dashReady) return;
  dashReady = true;

  document.getElementById('today-date').textContent = new Date().toLocaleDateString('en-IN',{day:'numeric',month:'short',year:'numeric'});
  const total = sampleData.length;
  const high = sampleData.filter(d=>d.risk==='high').length;
  const safe = sampleData.filter(d=>d.risk==='safe').length;
  const avgScore = Math.round(sampleData.reduce((s,d)=>s+d.score,0)/total);

  animCount('m1',total,0,'');
  setTimeout(()=>animCount('m2',Math.round(high/total*100),0,'%'),200);
  setTimeout(()=>animCount('m3',Math.round(safe/total*100),0,'%'),400);
  setTimeout(()=>animCount('m4',avgScore,0,''),600);

  // Table
  renderTable(sampleData);

  // Trend chart
  if(trendChartInst) trendChartInst.destroy();
  trendChartInst = new Chart(document.getElementById('trendChart'),{
    type:'line',
    data:{
      labels:['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],
      datasets:[
        {label:'Total',data:[8,12,7,15,10,5,3],borderColor:'#7c3aed',backgroundColor:'rgba(124,58,237,0.1)',fill:true,tension:0.4,borderWidth:2},
        {label:'Fake',data:[4,8,3,10,7,3,2],borderColor:'#ef4444',backgroundColor:'rgba(239,68,68,0.08)',fill:true,tension:0.4,borderWidth:2}
      ]
    },
    options:{
      responsive:true,maintainAspectRatio:false,
      plugins:{legend:{display:false}},
      scales:{
        x:{ticks:{color:'#9d89c4'},grid:{color:'rgba(255,255,255,0.05)'}},
        y:{ticks:{color:'#9d89c4'},grid:{color:'rgba(255,255,255,0.05)'}}
      }
    }
  });

  // Admin pie
  if(adminPieChartInst) adminPieChartInst.destroy();
  adminPieChartInst = new Chart(document.getElementById('adminPieChart'),{
    type:'doughnut',
    data:{
      labels:['Safe','Suspicious','High Risk'],
      datasets:[{data:[safe,sampleData.filter(d=>d.risk==='suspicious').length,high],backgroundColor:['#10b981','#f59e0b','#ef4444'],borderWidth:0,hoverOffset:4}]
    },
    options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},cutout:'65%'}
  });

  // Keywords
  const kwMax = keywords_freq[0].count;
  document.getElementById('kw-list').innerHTML = keywords_freq.map(k=>`
    <div class="kw-item">
      <div class="kw-label">${k.kw}</div>
      <div class="kw-bar-bg"><div class="kw-bar" style="width:${(k.count/kwMax*100).toFixed(0)}%"></div></div>
      <div class="kw-count">${k.count}</div>
    </div>`).join('');

  // Heatmap
  const intensities = [2,8,5,12,7,3,1, 4,10,6,15,9,2,0, 6,11,8,13,7,4,2, 3,7,5,10,12,5,1, 2,9,6,14,8,3,1];
  const maxI = Math.max(...intensities);
  const cols = ['rgba(124,58,237,0.1)','rgba(124,58,237,0.3)','rgba(124,58,237,0.5)','rgba(124,58,237,0.7)','rgba(124,58,237,0.9)'];
  document.getElementById('heatmap').innerHTML = intensities.map(v=>{
    const idx = Math.floor(v/maxI*4);
    return `<div class="hm-cell" style="background:${cols[idx]}" title="${v} submissions"></div>`;
  }).join('');
}

let allData = [...sampleData];
function renderTable(data) {
  document.getElementById('table-body').innerHTML = data.map((d,i)=>`
    <tr>
      <td style="color:var(--text-muted)">${i+1}</td>
      <td style="font-weight:500">${d.company}</td>
      <td style="color:var(--text-muted)">${d.role}</td>
      <td><span class="score-pill" style="color:${d.risk==='safe'?'#10b981':d.risk==='suspicious'?'#f59e0b':'#ef4444'}">${d.score}%</span></td>
      <td><span class="badge badge-${d.risk}">${d.risk==='high'?'High Risk':d.risk.charAt(0).toUpperCase()+d.risk.slice(1)}</span></td>
      <td>${d.fee>0?'₹'+d.fee.toLocaleString():'Free'}</td>
      <td style="color:var(--text-muted)">${d.date}</td>
    </tr>`).join('');
}
function filterTable(q) {
  const filtered = allData.filter(d=>d.company.toLowerCase().includes(q.toLowerCase())||d.role.toLowerCase().includes(q.toLowerCase()));
  renderTable(filtered);
}
function filterByRisk(r) {
  renderTable(r==='all'?allData:allData.filter(d=>d.risk===r));
}
function setDashSection(el) {
  document.querySelectorAll('.sidebar-item').forEach(i=>i.classList.remove('active'));
  el.classList.add('active');
}

// ─── TOAST ────────────────────────────────────────────────────
function showToast(msg, type='info') {
  const icons = {success:'✅',error:'❌',info:'ℹ️'};
  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  toast.innerHTML = `<span class="toast-icon">${icons[type]}</span><span class="toast-text">${msg}</span>`;
  document.getElementById('toasts').appendChild(toast);
  setTimeout(()=>toast.remove(), 4000);
}

// ─── PDF EXPORT ───────────────────────────────────────────────
function exportPDF() {
  showToast('📄 Generating PDF report...','info');
  setTimeout(()=>showToast('PDF report downloaded successfully!','success'),1500);
}

// ─── INIT ─────────────────────────────────────────────────────
animateCounters();
</script>
</body>
</html>
