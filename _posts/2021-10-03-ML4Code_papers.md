---
layout: post
title: "Deep Learning for Code: a Collection of Papers"
tags: code-understanding ml4code
---

In this post, I try to list every ML/DL paper that target code understanding, code representation, and bug finding. Despite my efforts to compile an exhaustive list, there are definitely ones that I have missed. Please email me if you find a paper that is missing. I will keep this post up-to-date as I continue my studies.

Every top-level category consists of the papers that were published in a specific year. Under some of the paper descriptions, I have added a few keywords about the ideas and tasks.


## 2021
- **Language-agnostic representation learning of source code from structure and context**\
Zugner, Daniel and Kirschstein, Tobias and Catasta, Michele and Leskovec, Jure and Gunnemann, Stephan\
arXiv preprint arXiv:2103.11318\
ICLR\
``{model: , tasks: , representation: , highlights: }``

- **Evaluating large language models trained on code**\
Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Ponde, Henrique and Kaplan, Jared and Edwards, Harri and Burda, Yura and Joseph, Nicholas and Brockman, Greg and others\
arXiv preprint arXiv:2107.03374

- **More with less: Exploring how to use deep learning effectively through semi-supervised learning for automatic bug detection in student code.**\
Shi, Yang and Mao, Ye and Barnes, Tiffany and Chi, Min and Price, Thomas W\
In Proceedings of the 14th International Conference on Educational Data Mining (EDM)\

- **Fast and memory-efficient neural code completion**\
Svyatkovskiy, Alexey and Lee, Sebastian and Hadjitofi, Anna and Riechert, Maik and Franco, Juliana Vicente and Allamanis, Miltiadis\
2021 IEEE/ACM 18th International Conference on Mining Software Repositories (MSR)\
`{model: , tasks: code completion, representation: embeds subtokens, highlights: }`

- **CCMC: Code Completion with a Memory Mechanism and a Copy Mechanism**\
Yang, Hao and Kuang, Li\
Evaluation and Assessment in Software Engineering\
`{model: transformer-XL, tasks: , representation: sequence of AST nodes in in-order DFS fashion, highlights: long-range dependencies but consumes a lot of memory and compute resources}`

- **Studying the usage of text-to-text transfer transformer to support code-related tasks**\
Mastropaolo, Antonio and Scalabrino, Simone and Cooper, Nathan and Palacio, David Nader and Poshyvanyk, Denys and Oliveto, Rocco and Bavota, Gabriele\
2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE)\

- **InferCode: Self-Supervised Learning of Code Representations by Predicting Subtrees**\
Bui, Nghi DQ and Yu, Yijun and Jiang, Lingxiao\
2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE)\
`{model: Tree-based CNN, tasks: , representation: subtrees of an AST--traverses AST and for specific nodes such as stmts extracts subtree rooted at the visited node then makes a vocab of subtrees-->so the model's job would be to predict subtrees given an AST, highlights: unsupervised so helps with scarcity of labeled data, pretraining}`

- **PSIMiner: A Tool for Mining Rich Abstract Syntax Trees from Code**\
Spirin, Egor and Bogomolov, Egor and Kovalenko, Vladimir and Bryksin, Timofey\
arXiv preprint arXiv:2103.12778\

- **A Survey on Software Defect Prediction Using Deep Learning**\
Akimova, Elena N and Bersenev, Alexander Yu and Deikov, Artem A and Kobylkin, Konstantin S and Konygin, Anton V and Mezentsev, Ilya P and Misilov, Vladimir E\
Multidisciplinary Digital Publishing Institute

- **A large-scale benchmark for few-shot program induction and synthesis**\
Alet, Ferran and Lopez-Contreras, Javier and Koppel, James and Nye, Maxwell and Solar-Lezama, Armando and Lozano-Perez, Tomas and Kaelbling, Leslie and Tenenbaum, Joshua\
International Conference on Machine Learning

- **On the Effectiveness of Deep Vulnerability Detectors to Simple Stupid Bug Detection**\
Hua, Jiayi and Wang, Haoyu\
2021 IEEE/ACM 18th International Conference on Mining Software Repositories (MSR)

- **BERT2Code: Can Pretrained Language Models be Leveraged for Code Search?**\
Ishtiaq, Abdullah Al and Hasan, Masum and Haque, Md and Anjum, Mahim and Mehrab, Kazi Sajeed and Muttaqueen, Tanveer and Hasan, Tahmid and Iqbal, Anindya and Shahriyar, Rifat\
arXiv preprint arXiv:2104.08017\
`{model: code2vec/codebert to embed source code and a simple NN with 2 hidden layers to embed NL query, tasks: , representation: , highlights: learns a mapping between NL embeddings and code embeddings}`

- **On the generalizability of Neural Program Models with respect to semantic-preserving program transformations**\
Rabin, Md Rafiqul Islam and Bui, Nghi DQ and Wang, Ke and Yu, Yijun and Jiang, Lingxiao and Alipour, Mohammad Amin\
Information and Software Technology\
`{model: , tasks: , representation: , highlights: robustness study}`

- **Do Transformers Really Perform Bad for Graph Representation?**\
Ying, Chengxuan and Cai, Tianle and Luo, Shengjie and Zheng, Shuxin and Ke, Guolin and He, Di and Shen, Yanming and Liu, Tie-Yan\
arXiv preprint arXiv:2106.05234\
`{model: transformer for graphs, tasks: , representation: , highlights: they call it Graphormer}`

- **TFix: Learning to Fix Coding Errors with a Text-to-Text Transformer**\
Berabi, Berkay and He, Jingxuan and Raychev, Veselin and Vechev, Martin\
International Conference on Machine Learning (PMLR)\
`{model: transformer, tasks: fixing code errors, representation: sequence of tokens, features: }`

- **Generating Adversarial Computer Programs using Optimized Obfuscations**\
Srikant, Shashank and Liu, Sijia and Mitrovska, Tamara and Chang, Shiyu and Fan, Quanfu and Zhang, Gaoyuan and O'Reilly, Una-May\\
arXiv preprint arXiv:2103.11882\
`{model: , tasks: , representation: , highlights: focuses on adversarial robustness}`

- **Self-Supervised Bug Detection and Repair**\
Allamanis, Miltiadis and Jackson-Flux, Henry and Brockschmidt, Marc\
arXiv preprint arXiv:2105.12787\
`{model: GNN, tasks: , representation: AST augmented with control and dataflow edges, features: defines the graph as entities and relations, works better than CuBERT and GREAT on real bugs, self-supervised.}`

- **How could Neural Networks understand Programs?**\
Peng, Dinglan and Zheng, Shuxin and Li, Yatao and Ke, Guolin and He, Di and Liu, Tie-Yan\
arXiv preprint arXiv:2105.04297\
`{model: transformer, tasks: , representation: control flow of LLVM IR, highlights: }`

- **Code prediction by feeding trees to transformers**\
Kim, Seohyun and Zhao, Jinman and Tian, Yuchi and Chandra, Satish\
2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE)\
`{model: transformer, tasks: , representation: 1) token sequence or 2) AST node sequence in pre-order fashion or 3) root-to-leaf paths, highlights: makes the transformer aware of the syntactic structure of code i.e. improves self attention block similar to GREAT}`

- **CLSEBERT: Contrastive Learning for Syntax Enhanced Code Pre-Trained Model**\
Wang, Xin and Wang, Yasheng and Zhou, Pingyi and Xiao, Meng and Wang, Yadao and Li, Li and Liu, Xiao and Wu, Hao and Liu, Jin and Jiang, Xi\
arXiv preprint arXiv:2108.04556\
`{model: , tasks: , representation: AST as sequence, highlights: pretraining, noise invariant code representation using contrastive learning by introducing noise into input sequence at training time, focus on robustness}`

- **CoTexT: Multi-task Learning with Code-Text Transformer**\
Phan, Long and Tran, Hieu and Le, Daniel and Nguyen, Hieu and Anibal, James and Peltekian, Alec and Ye, Yanfang\
arXiv preprint arXiv:2105.08645\
`{model: transformer, tasks: , representation: sequence of tokens, highlights: focuses on NL-PL tasks, pretraining}`

- **A Mocktail of Source Code Representations**\
Vagavolu, Dheeraj and Swarna, Karthik Chandra and Chimalakonda, Sridhar\
arXiv preprint arXiv:2106.10918\
`{model: , tasks: , representation: AST+CFG+PDG, highlights: an extension of code2vec}`

- **Program Synthesis with Large Language Models**\
Austin, Jacob and Odena, Augustus and Nye, Maxwell and Bosma, Maarten and Michalewski, Henryk and Dohan, David and Jiang, Ellen and Cai, Carrie and Terry, Michael and Le, Quoc and Sutton, Charles\
arXiv preprint arXiv:2108.07732

- **Automatic Code Generation using Pre-Trained Language Models**\
Ottens, Lizi and Perez, Luis and Viswanathan, Sudharshan\
arXiv preprint arXiv:2102.10535

- **SySeVR: A framework for using deep learning to detect software vulnerabilities**\
Li, Zhen and Zou, Deqing and Xu, Shouhuai and Jin, Hai and Zhu, Yawei and Chen, Zhaoxuan\
IEEE Transactions on Dependable and Secure Computing

## 2020
- **Structural language models of code**\
Alon, Uri and Sadaka, Roy and Levy, Omer and Yahav, Eran\
International Conference on Machine Learning\
`{model: , tasks: code generation, representation: paths from the root and leaves in AST, features: copy mechanism}`

- **DL-Droid: Deep learning based android malware detection using real devices**\
Alzaylaee, Mohammed K and Yerima, Suleiman Y and Sezer, Sakir\
Computers & Security, Elsevier\
`{model: , tasks: malware detection, representation: , features: hand-engineered and heuristic-based}`

- **DRAST--A Deep Learning and AST Based Approach for Bug Localization**\
Sangle, Shubham and Muvva, Sandeep and Chimalakonda, Sridhar and Ponnalagu, Karthikeyan and Venkoparao, Vijendran Gopalan\
arXiv preprint arXiv:2011.03449\
`{model: , tasks: , representation: AST, highlights: }`

- **Backdoors in neural models of source code**\
Ramakrishnan, Goutham and Albarghouthi, Aws\
arXiv preprint arXiv:2006.06841\
`{model: , tasks: , representation: , highlights: adversarial robustness}`

- **Adversarial examples for models of code**\
Yefet, Noam and Alon, Uri and Yahav, Eran\
Proceedings of the ACM on Programming Languages (OOPSLA)\
`{model: , tasks: , representation: , highlights: adversarial robustness}`

- **Semantic robustness of models of source code**\
Ramakrishnan, Goutham and Henkel, Jordan and Wang, Zi and Albarghouthi, Aws and Jha, Somesh and Reps, Thomas\
arXiv preprint arXiv:2002.03043\
`{model: , tasks: , representation: , highlights: focuses on semantic robustness and training with semantic-preserving code transformations}`

- **Software vulnerability detection using deep neural networks: A survey**\
Lin, Guanjun and Wen, Sheng and Han, Qing-Long and Zhang, Jun and Xiang, Yang\
Proceedings of the IEEE

- **Approaches for Representing Software as Graphs for Machine Learning Applications**\
Romanov, Vitaly and Ivanov, Vladimir and Succi, Giancarlo\
2020 International Computer Symposium (ICS)


- **TranS^3: A transformer-based framework for unifying code summarization and code search**\
Wang, Wenhua and Zhang, Yuqun and Zeng, Zhengran and Xu, Guandong\
arXiv preprint arXiv:2003.03238\
`{model: transformer, tasks: code search and summarization, representation: AST, highlights: unifying framework for both code searching and summarization}`

- **Multi-task learning based pre-trained language model for code completion**\
Liu, Fang and Li, Ge and Zhao, Yunfei and Jin, Zhi\
Proceedings of the 35th IEEE/ACM International Conference on Automated Software Engineering**\
`{model: transformer, tasks: code completion, representation: , highlights: pretraining}`

- **Language Modelling for Source Code with Transformer-XL**\
Dowdell, Thomas and Zhang, Hongyu\
arXiv preprint arXiv:2007.15813\
`{model: transformer-XL, tasks: , representation: , highlights: language modeling for source code, increase context size}`

- **Big code != big vocabulary: Open-vocabulary models for source code**\
Karampatsis, Rafael-Michael and Babii, Hlib and Robbes, Romain and Sutton, Charles and Janes, Andrea\
2020 IEEE/ACM 42nd International Conference on Software Engineering (ICSE)

- **Scelmo: Source code embeddings from language models\
Karampatsis, Rafael-Michael and Sutton, Charles\
arXiv preprint arXiv:2004.13214

- **DeepVS: an efficient and generic approach for source code modelling usage**\
Hussain, Yasir and Huang, Zhiqiu and Zhou, Yu and Wang, Senzhang\
Electronics Letters, Wiley Online Library

- **Dlfix: Context-based code transformation learning for automated program repair**\
Li, Yi and Wang, Shaohua and Nguyen, Tien N\
Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering\
`{model: tree-based LSTM, tasks: , representation: AST, highlights: learning transformations to fix code instead of seq2seq}`

- **Compiler-based graph representations for deep learning models of code**\
Brauckmann, Alexander and Goens, Andr{\'es and Ertel, Sebastian and Castrillon, Jeronimo\
Proceedings of the 29th International Conference on Compiler Construction\
`{model: GNN, tasks: , representation: AST and control flow edges, highlights: }`

- **Deep learning for source code modeling and generation: Models, applications, and challenges**\
Le, Triet HM and Chen, Hao and Babar, Muhammad Ali\
ACM Computing Surveys (CSUR)

- **Duplicate bug report detection and classification system based on deep learning technique**\
Kukkar, Ashima and Mohana, Rajni and Kumar, Yugal and Nayyar, Anand and Bilal, Muhammad and Kwak, Kyung-Sup\
IEEE Access

- **A self-attentional neural architecture for code completion with multi-task learning**\
Liu, Fang and Li, Ge and Wei, Bolin and Xia, Xin and Fu, Zhiyi and Jin, Zhi\
Proceedings of the 28th International Conference on Program Comprehension\
`{model: , tasks: code completion, representation: AST nodes as an ordered sequences to root, highlights: }`

- **A transformer-based approach for source code summarization**\
Ahmad, Wasi Uddin and Chakraborty, Saikat and Ray, Baishakhi and Chang, Kai-Wei\
arXiv preprint arXiv:2005.00653\
`{model: transformer, tasks: code summarization, representation: pairwise relationships between tokens based on AST, features: long-range}`

- **Software defect prediction via transformer**\
Zhang, Qihang and Wu, Bin\
2020 IEEE 4th Information Technology, Networking, Electronic and Automation Control Conference (ITNEC)\
`{model: transformer, tasks: , representation: AST, highlights: }`

- **Adversarial robustness for code**\
Bielik, Pavol and Vechev, Martin\
International Conference on Machine Learning (PMLR)\
`{model: , tasks: , representation: , highlights: focus on adversarial robustness of code}`

- **Modular tree network for source code representation learning**\
Wang, Wenhan and Li, Ge and Shen, Sijie and Xia, Xin and Jin, Zhi\
ACM Transactions on Software Engineering and Methodology (TOSEM)\
`{model: tree-LSTM, tasks: , representation: AST, highlights: it is a modular tree network extracted from AST}`

- **IntelliCode Compose: Code generation using transformer**\
Svyatkovskiy, Alexey and Deng, Shao Kun and Fu, Shengyu and Sundaresan, Neel\
Proceedings of the 28th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering\
`{model: transformer, tasks: code generation, representation: , highlights: they call the model GPT-C}`

- **Automated vulnerability detection in source code using minimum intermediate representation learning**\
Li, Xin and Wang, Lu and Xin, Yang and Yang, Yixian and Chen, Yuling\
Applied Sciences, Multidisciplinary Digital Publishing Institute

- **Hoppity: Learning graph transformations to detect and fix bugs in programs**\
Dinella, Elizabeth and Dai, Hanjun and Li, Ziyang and Naik, Mayur and Song, Le and Wang, Ke\
International Conference on Learning Representations (ICLR)\
`{model: GNN, tasks: fixing bugs, representation: AST with subtoken cache, highlights: }`

- **CodeBERT: A pre-trained model for programming and natural languages**\
Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and others\
arXiv preprint arXiv:2002.08155\
`{model: transformer, tasks: code search, representation: , highlights: bimodal pretrained model for PL/NL}`

- **GraphcodeBERT: Pre-training code representations with data flow**\
Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and others\
arXiv preprint arXiv:2009.08366\
`{model: transformer, tasks: code refinement, representation: , highlights: pretraining, similar to codebert but uses dataflow info at pretraining}`

## 2019
- **Synthetic datasets for neural program synthesis**\
Shin, Richard and Kant, Neel and Gupta, Kavi and Bender, Christopher and Trabucco, Brandon and Singh, Rishabh and Song, Dawn\
arXiv preprint arXiv:1912.12345\
2019

- **PathMiner: a library for mining of path-based representations of code**\
Kovalenko, Vladimir and Bogomolov, Egor and Bryksin, Timofey and Bacchelli, Alberto\
2019 IEEE/ACM 16th International Conference on Mining Software Repositories (MSR)\
2019

- **A hybrid deep learning image-based analysis for effective malware detection**\
Venkatraman, Sitalakshmi and Alazab, Mamoun and Vinayakumar, R\
Journal of Information Security and Applications, Elsevier\
2019

- **Pre-trained language model representations for language generation**\
Edunov, Sergey and Baevski, Alexei and Auli, Michael\
arXiv preprint arXiv:1903.09722\
2019

- **Multi-modal attention network learning for semantic source code retrieval**\
Wan, Yao and Shu, Jingdong and Sui, Yulei and Xu, Guandong and Zhao, Zhou and Wu, Jian and Yu, Philip S\
arXiv preprint arXiv:1909.13516\
2019

- **A zero-positive learning approach for diagnosing software performance regressions**\
Alam, Mejbah and Gottschlich, Justin and Tatbul, Nesime and Turek, Javier S and Mattson, Tim and Muzahid, Abdullah\
Advances in Neural Information Processing Systems\
2019

- **code2vec: Learning distributed representations of code**\
Alon, Uri and Zilberstein, Meital and Levy, Omer and Yahav, Eran\
Proceedings of the ACM on Programming Languages\
`{model: , tasks: , representation: pairwise paths between AST terminal nodes, highlights: }`

- **Deep-autocoder: Learning to complete code precisely with induced code tokens**\
Hu, Xing and Men, Rui and Li, Ge and Jin, Zhi\
2019 IEEE 43rd Annual Computer Software and Applications Conference (COMPSAC)\
`{model: LSTM, tasks: , representation: AST, highlights: learn language models over code corpus}`

- **Pythia: AI-assisted code completion system**\
Svyatkovskiy, Alexey and Zhao, Ying and Fu, Shengyu and Sundaresan, Neel\
Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining\
`{model: LSTM, tasks: code completion, representation: serialized AST, highlights: }`

- **Maybe deep neural networks are the best choice for modeling source code**\
Karampatsis, Rafael-Michael and Sutton, Charles\
arXiv preprint arXiv:1903.05734

- **Structural language models for any-code generation**\
Alon, Uri and Sadaka, Roy and Levy, Omer and Yahav, Eran

- **A novel neural source code representation based on abstract syntax tree**\
Zhang, Jian and Wang, Xu and Zhang, Hongyu and Sun, Hailong and Wang, Kaixuan and Liu, Xudong\
2019 IEEE/ACM 41st International Conference on Software Engineering (ICSE)\
`{model: RNN, tasks: , representation: AST split into a sequence of small stmt-level subtrees, highlights: }`

- **IdBench: Evaluating Semantic Representations of Identifier Names in Source Code**\
Wainakh, Yaza and Rauf, Moiz and Pradel, Michael\
arXiv preprint arXiv:1910.05177

- **Neural program repair by jointly learning to localize and repair**\
Vasic, Marko and Kanade, Aditya and Maniatis, Petros and Bieber, David and Singh, Rishabh\
arXiv preprint arXiv:1904.01720

- **Open vocabulary learning on source code with a graph-structured cache**\
Cvitkovic, Milan and Singh, Badal and Anandkumar, Animashree\
International Conference on Machine Learning (PMLR)\
`{model: GNN, tasks: , representation: augmented AST, highlights: add a graph-structural vocabulary cache to the graph--add edges from a subtoken vocab to terminal nodes}`

- **A literature study of embeddings on source code**\
Chen, Zimin and Monperrus, Martin\
arXiv preprint arXiv:1904.03061

- **Devign: Effective vulnerability identification by learning comprehensive program semantics via graph neural networks**\
Zhou, Yaqin and Liu, Shangqing and Siow, Jingkai and Du, Xiaoning and Liu, Yang\
arXiv preprint arXiv:1909.03496\
`{model: GNN, tasks: , representation: AST, highlights: }`

- **Global Relational Models of Source Code**\
Hellendoorn, Vincent J and Sutton, Charles and Singh, Rishabh and Maniatis, Petros and Bieber, David\
International conference on learning representations\
`{model: transformer with attention bias, tasks: varmisuse, representation: sequence of tokens but incorporating semantically meaningful relations, highlights: longer-range dependencies compared to transformer but still limited by context-size}`

- **Learning a static bug finder from data**\
Wang, Yu and Gao, Fengjuan and Wang, Linzhang and Wang, Ke\
arXiv preprint arXiv:1907.05579\
`{model: GNN, tasks: , representation: augmented AST, highlights: split the code graph into multiple disjoint ones, suitable for more complex bugs such as null pointer deref, less accurate when handling large programs (large = 1000 nodes)}`

- **Deep learning for bug-localization in student programs**\
Gupta, Rahul and Kanade, Aditya and Shevade, Shirish\
arXiv preprint arXiv:1905.12454\
`{model: tree convolutional neural network, tasks: bug localization, representation: AST, highlights: }`

- **A comprehensive study on deep learning bug characteristics**\
Islam, Md Johirul and Nguyen, Giang and Pan, Rangeet and Rajan, Hridesh\
Proceedings of the 2019 27th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering

## 2018
- **Deepbugs: A learning approach to name-based bug detection**\
Pradel, Michael and Sen, Koushik\
Proceedings of the ACM on Programming Languages (OOPSLA)\
`{model: , tasks: , representation: embed only program identifiers in a list, highlights: }`

- **code2seq: Generating sequences from structured representations of code**\
Alon, Uri and Brody, Shaked and Levy, Omer and Yahav, Eran\
arXiv preprint arXiv:1808.01400\
`{model: , tasks: code captioning, representation: all pairwise paths between terminal nodes in AST, features: }`

## 2017
- **Learning to Represent Student Knowledge on Programming Exercises Using Deep Learning**\
Wang, Lisa and Sy, Angela and Liu, Larry and Piech, Chris\
International Educational Data Mining Society

- **Pallas: Semantic-aware checking for finding deep bugs in fast path**\
Huang, Jian and Allen-Bond, Michael and Zhang, Xuechen\
Proceedings of the Twenty-Second International Conference on Architectural Support for Programming Languages and Operating Systems

- **Learning to represent programs with graphs**\
Allamanis, Miltiadis and Brockschmidt, Marc and Khademi, Mahmoud\
arXiv preprint arXiv:1711.00740\
`{model: GGNN, tasks: varmisuse, representation: AST augmented with control and dataflow, features: }`

- **DeepFix: Fixing common C language errors by deep learning**\
Gupta, Rahul and Pal, Soham and Kanade, Aditya and Shevade, Shirish\
Thirty-First AAAI Conference on Artificial Intelligence\
`{model: multi-layered seq2seq neural network with attention, tasks: bug finding and fixing, representation: token sequence, highlights: }`

- **Inductive representation learning on large graphs**\
Hamilton, William L and Ying, Rex and Leskovec, Jure\
Proceedings of the 31st International Conference on Neural Information Processing Systems

- **Code completion with neural attention and pointer networks**\
Li, Jian and Wang, Yue and Lyu, Michael R and King, Irwin\
arXiv preprint arXiv:1711.09573\
`{model: , tasks: , representation: flattened AST, highlights: }`

- **Program synthesis from natural language using recurrent neural networks**\
Lin, Xi Victoria and Wang, Chenglong and Pang, Deric and Vu, Kevin and Ernst, Michael D\
University of Washington Department of Computer Science and Engineering, Seattle, WA, USA, Tech. Rep. UW-CSE-17-03-01\
`{model: RNN encoder-decoder, tasks: program synthesis from NL, representation: , highlights: generates a program template from NL sentence}`

## 2016
- **Program synthesis using natural language**\
Desai, Aditya and Gulwani, Sumit and Hingorani, Vineet and Jain, Nidhi and Karkare, Amey and Marron, Mark and Roy, Subhajit\
Proceedings of the 38th International Conference on Software Engineering

- **Neuro-symbolic program synthesis**\
Parisotto, Emilio and Mohamed, Abdel-rahman and Singh, Rishabh and Li, Lihong and Zhou, Dengyong and Kohli, Pushmeet\
arXiv preprint arXiv:1611.01855

- **Summarizing source code using a neural attention model**\
Iyer, Srinivasan and Konstas, Ioannis and Cheung, Alvin and Zettlemoyer, Luke\
Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)


## 2013
- **Mantis: Automatic performance prediction for smartphone applications**\
Kwon, Yongin and Lee, Sangmin and Yi, Hayoon and Kwon, Donghyun and Yang, Seungjun and Chun, Byung-Gon and Huang, Ling and Maniatis, Petros and Naik, Mayur and Paek, Yunheung\
USENIX Annual Technical Conference 13







