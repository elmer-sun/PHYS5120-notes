# PHYS5120 中文自学教材

本目录是当前课程教材的主稿，统一先写**中文 LaTeX**。唯一编译入口为 [main.tex](main.tex)，公共排版与符号在 [preamble.tex](preamble.tex)。[中文 PDF](PHYS5120-中文教材.pdf) 用于阅读；修改以 LaTeX 源文件为准。原始协作笔记来自 [Overleaf 项目](https://www.overleaf.com/project/6130625f9c31a759aa64b17b)，原贡献者权益保留；本地修改不自动同步到 Overleaf。

## 长期写作纲领

以 **Cohen–Tannoudji《Quantum Mechanics》的教学品质**为标杆，独立编写适合系统自学的研究生级教材，不做知识点总结、讲义摘录或百科条目。这是所有后续章节修改的约束，不是本次修改的临时文风。

1. **从基础出发，循序渐进。** 假定读者聪明、有基本数学能力，但对当前主题几乎一无所知。首次出现的符号、概念和必要前置知识要先解释；宁可细讲，不留逻辑跳跃。
2. **以问题驱动理论。** 先交代正在解决什么问题、已有知识为什么不够，以及新概念为何自然出现，再给定义与数学形式。不能让公式凭空出现。
3. **推导完整严谨。** 明确假设、定义与适用范围。重要公式逐步推导，不能以“显然”“容易得到”或把关键证明留给读者来遮蔽难点。数学步骤与物理意义相互支撑。
4. **建立可迁移的直觉。** 不只给结论，还解释为什么、如何理解、与已有知识的联系。使用简单模型、具体例子、极限与反例检验理解。
5. **保持教材可读性。** 采用自然、连贯、耐心的中文叙述，段落之间有因果与问题承接；避免频繁项目符号、碎片短句、空泛总结和机械的“定义—公式—结论”。
6. **体系完整而不堆砌。** 先建理论骨架，再加入复杂情形、推广与深入讨论。安排明确的知识依赖，使读者可以从头顺畅学下来。
7. **起点低，终点不降低。** 从基础讲起不等于牺牲研究生及科研入门深度；通往深处的每一级台阶都要扎实。

最重要的判断标准：**不是让读者迅速知道有哪些知识，而是让一个原本不懂的人，沿自然且严密的逻辑真正掌握知识。** 写作时始终自问：首次接触这里的读者能理解为什么这样做吗？有没有隐含前置知识、跳过的推理或突兀概念？追求单位认知负担下的理解深度，而非信息密度最大化。

中文教材是当前唯一扩写主线，不再遵循旧版“保持英文”的约定。`../讲义/笔记/` 的 Markdown 保留为早期课程资料整理，按需核对，不平行维护同一份教材正文。

## 阅读与编辑顺序

|章|正文|问题|
|---|---|---|
|1|[统计与分子动力学](chapters/01-molecular-dynamics.tex)|如何由轨迹得到平均，如何稳定推进轨迹？|
|2|[力场与输运](chapters/02-force-fields-and-transport.tex)|有限模拟盒怎样代表材料，输出如何转为性质？|
|3|[Monte Carlo](chapters/03-monte-carlo.tex)|只求平衡时怎样设计采样？|
|4|[Born–Oppenheimer：电子与核分离](chapters/04-adiabatic-approximation.tex)|电子怎样产生核的势能面？|
|5|[固定核多电子问题：Hartree 与 Hartree–Fock](chapters/05-hartree-fock.tex)|如何构造可解的多电子近似？|
|6|[电子关联](chapters/06-electronic-correlation.tex)|单行列式遗漏什么，怎样补回？|
|7|[密度泛函基础](chapters/07-density-functional-theory.tex)|为什么可以用密度，怎样得到 KS 方程？|
|8|[交换关联近似](chapters/08-exchange-correlation-functionals.tex)|未知泛函如何变为具体模型？|
|9|[轨道能量与带隙](chapters/09-kohn-sham-spectra.tex)|哪些本征值具有物理意义？|
|10|[周期固体与基组](chapters/10-solids-and-basis-sets.tex)|怎样计算无限晶体？|
|11|[晶格振动](chapters/11-frozen-phonons.tex)|能量曲率如何决定稳定性和声子？|
|12|[Car–Parrinello](chapters/12-car-parrinello.tex)|怎样连接电子求解与核动力学？|

当前优先优化朋友笔记覆盖的第 1–9 章，补齐其中理解主线所必需的基础与推导。第 10–12 章已有稿保留，暂不扩写；笔记未记录的新专题也暂不铺开。先保证现有内容能循序读通，再扩大范围。

电子结构的依赖顺序是：**电子与核的完整问题 → Born–Oppenheimer 分离 → 固定核多电子 Hamilton 算符 → 变分原理 → Hartree → 反对称性与 Hartree–Fock → 超越 HF 的关联 → DFT**。BO 处理电子与核运动的耦合，Hartree/HF 处理给定核构型下的电子问题；两层近似必须分开说明。量子内积、本征态及相关记号在第 4 章首次使用前引入。

## 来源、核对程度与边界

朋友的 `../Computational Physics.pdf` 共 50 页，2026-11-05 已逐页转成 PNG 并逐页目视阅读，未用文字提取冒充图像阅读。逐页内容、对应正文和纠错依据见 [来源核对](source-review.md)。封面为第 1 页，第 50 页空白。第 10–12 章超出该 PDF 的范围，来自原英文稿的独立中文重写，不能宣称朋友笔记为这些章节提供了验证。

当前是覆盖原有 12 章主线的中文教材初稿，已经补写重要推导并修正识别出的公式与概念错误，但还不能称为完成同行评审的研究生教材。后续可能需要深入的内容包括（并非当前已授权扩大范围的任务）：线性响应与热流的完整微观推导、均匀气交换积分、非局域相关与 RPA、赝势构造与可转移性实例、完整算例与习题。现有内容明确说明这些边界，不以术语出现代替掌握。原讲义 Lec9 的可复现性专题目前仍在旧 Markdown 笔记中，本次没有冒称已经收入中文 LaTeX 全书。

原英文稿保存在 Git 历史 `0765a746fb5a58fdc82760d74b6f8dff85752fb6`，原始图像保留在 `figures/`，未删除。原 PDF 与讲义保持不变。不要为每次修改另造教材副本。

## 编译与核验

在本目录用 **XeLaTeX** 编译，不再使用旧版 pdfLaTeX 命令。临时文件放项目外，例如 PowerShell：

```powershell
$buildDir = Join-Path $env:TEMP 'phys5120-review/build'
New-Item -ItemType Directory -Force $buildDir | Out-Null
xelatex -interaction=nonstopmode -halt-on-error "-output-directory=$buildDir" main.tex
xelatex -interaction=nonstopmode -halt-on-error "-output-directory=$buildDir" main.tex
Copy-Item -LiteralPath (Join-Path $buildDir 'main.pdf') -Destination 'PHYS5120-中文教材.pdf'
```

首轮或目录变动后可能需要第三次编译。交付前检查交叉引用、缺字与超宽公式，并把生成 PDF 渲染为图片检查。新增公式标签使用章节前缀；同一符号跨章改变意义时须明说。电子结构第 5 章起默认原子单位，出现 SI 或显式 ħ 时说明用途。仅提交本次相关改动，不自动推送。
