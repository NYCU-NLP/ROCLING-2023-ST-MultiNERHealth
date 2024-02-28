# ROCLING 2023 Shared Task for Chinese Multi-genre Named Entity Recognition in the Healthcare Domain (MultiNER-Health)
The goal of the MultiNER-Health shared task is to develop and evaluate the capability of Chinese NER systems for healthcare texts written in different genres. The input is a sentence indicating as one of three genres (i.e., FT, SM, and WA) that may contain named entities. The NER system should predict the boundaries and category of the named entity for each sentence.
Following the settings of the ROCLING-2022 shared task (Lee et al., 2022), we use the common BIO format for our MultiNER-Health task. The B (Beginning)-prefix before a tag indicates that the character is the beginning of a named entity while the I (Inside)-prefix indicates that the character is inside a named entity, and O (Outside) indicates that a character belongs to no named entity. We use the same entity types defined in the Chinese HealthNER Corpus (Lee and Lu, 2021). A total of 10 types are described for this Chinese healthcare NER task, and some examples are provided in Table 1. 

|  Entity Type (Tag)   | Description  |   Examples  |
|  :----:  | ----  | ----  | 
| Body (BODY)  | The whole physical structure that forms a personor animal including biological cells, organizations, organs and systems. | “細胞核” (nucleus), “神經組織” (nerve tissue), “左心房” (left atrium), “脊髓” (spinal cord), “呼吸系統” (respiratory system) |
| Symptom (SYMP)  | Any feeling of illness or physical or mental change that is caused by a particular disease. | “流鼻水”(rhinorrhea), “咳嗽” (cough), “貧血” (anemia), “ 失眠 ” (insomnia), “ 心悸 ” (palpitation), “耳鳴” (tinnitus) |
| Instrument (INST)  | A tool or other device used for performing a particular medical task such as diagnosis and treatments. | “血壓計” (blood pressure meter), “達文西手臂” (DaVinci Robots), “體脂肪計” (body fat monitor), “雷射手術刀” (laser scalpel) |
| Examination (EXAM)  | The act of looking at or checking something carefully in order to discover possible diseases. |  “聽力檢查”(hearing test), “腦電波圖” (electroencephalography; EEG), “核磁共振造影” (magnetic resonance imaging; MRI) |
| Chemical (CHEM)  | Any basic chemical element typically found in the human body. | “去氧核糖核酸” (deoxyribonucleic acid; DNA), “糖化血色素” (glycated hemoglobin), “膽固醇” (cholesterol), “尿酸” (uric acid) |
| Disease (DISE)  | An illness of people or animals caused by infection or a failure of health rather than by an accident. | “小兒麻痺症” (poliomyelitis; polio), “帕金森氏症” (Parkinson’s disease), “青光眼” (glaucoma), “肺結核” (tuberculosis) |
| Drug (DRUG)  | Any natural or artificially made chemical used as a medicine. | “阿斯匹靈” (aspirin), “普拿疼” (acetaminophen), “青黴素” (penicillin), “流感疫苗” (influenza vaccination) |
| Supplement (SUPP)  | Something added to something else to improve human health. | “維他命” (vitamin), “膠原蛋白” (collagen), “益生菌 ” (probiotics), “葡萄糖胺” (glucosamine), “葉黃素” (lutein) |
| Treatment (TREAT)  | A method of behavior used to treat diseases. | “藥物治療” (pharmacotherapy), “胃切除術” (gastrectomy), “標靶治療” (targeted therapy), “外科手術” (surgery) |
| Time (TIME)   | Element of existence measured in minutes, days, years. | “嬰兒期” (infancy), “幼兒時期” (early childhood), “青春期” (adolescence), “生理期” (on one’s period), “孕期” (pregnancy) |

<p align="center">Table 1: Name entity types with descriptions and examples.</p>

## Examples
Example sentences are presented in Table 2. The input is a sentence consisting of a sequence of character-based tokens including punctuation. The NER system returns the corresponding BIO tags aligned to each token as the output. In the Example 1 from the FT genre, “老化” (aging) belongs to the Symptom (SYMP) entity type and “阿茲海默症” (Alzheimer’s disease) is a disease (DISE) type. “痤瘡” (acne) in Example 5 from the WA genre is also a kind of disease (DISE), and is a formal usage of “痘痘” in Example 2 from the SM genre. “燒心” in Example 6 from the WA genre is a spoken language form of a disease “胃食道逆流症” (gastroesophageal reflux disease) in Example 3 from the SM genre.
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Genre</th>
    <th class="tg-0pky">Examples</th>
    <th class="tg-0pky">Input &amp; Output</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky" rowspan="2">Formal<br>Texts<br>(FT)</td>
    <td class="tg-0pky">Ex 1</td>
    <td class="tg-0pky"><span style="font-style:italic">Input</span>: 早起也能預防老化，甚至降低阿茲海默症的風險<br><span style="font-style:italic">Output</span>:O, O, O, O, O, O, B-SYMP, I-SYMP, O, O, O, O, O, B-DISE, I- DISE, I-DISE, I-DISE, I-DISE, O, O, O</td>
  </tr>
  <tr>
    <td class="tg-0pky">Ex 2</td>
    <td class="tg-0pky"><span style="font-style:italic">Input</span>: 壓力、月經引起的痘痘患者<br><span style="font-weight:400;font-style:italic;text-decoration:none">Output</span><span style="font-weight:400;font-style:normal;text-decoration:none">: B-SYMP, I-SYMP, O, B-TIME, I-TIME, O, O, O, B-DISE, I- DISE, O, O</span></td>
  </tr>
  <tr>
    <td class="tg-0pky" rowspan="2">Social<br>Media<br>(SM)</td>
    <td class="tg-0pky">Ex 3</td>
    <td class="tg-0pky"><span style="font-style:italic">Input</span>: 如何治療胃食道逆流症?<br><span style="font-style:italic">Output</span>: O, O, O, O, B-DISE, I-DISE, I-DISE, I-DISE, I-DISE, I-DISE, O</td>
  </tr>
  <tr>
    <td class="tg-0pky">Ex 4</td>
    <td class="tg-0pky"><span style="font-style:italic">Input</span>: 請問長期打善思達針劑是不是會變胖?<br><span style="font-style:italic">Output</span>: O, O, O, O, O, B-DRUG, I-DRUG, I-DRUG, I-DRUG, I-DRUG, O, O, O, O, B-SYMP, I-SYMP, O</td>
  </tr>
  <tr>
    <td class="tg-0pky" rowspan="2">Wikipedia<br>Articles<br>(WA)</td>
    <td class="tg-0pky">Ex 5</td>
    <td class="tg-0pky"><span style="font-style:italic">Input</span>: 抗生素和維生素 A 酸可用於口服治療痤瘡<br><span style="font-style:italic">Output</span>: B-DRUG, I-DRUG, I-DRUG, O, B-DRUG, I-DRUG, I-DRUG, I- DRUG, I-DRUG, O, O, O, O, O, O, O, B-DISE, I-DISE</td>
  </tr>
  <tr>
    <td class="tg-0pky">Ex 6</td>
    <td class="tg-0pky"><span style="font-style:italic">Input</span>:抑酸劑，又稱抗酸劑，抑制胃酸分泌，緩解燒心<br><span style="font-style:italic">Output</span>: B-CHEM, I-CHEM, I-CHEM, O, O, O, B-CHEM, I-CHEM, I- CHEM, O, O, O, B-CHEM, I-CHEM, O, O, O, O, O, B-DISE, I-DISE</td>
  </tr>
</tbody>
</table>

<p align="center">Table 2: Examples of the MultiNER-Health task.</p>

# Data Preparation
The training sets for this MultiNER-health task consist of two parts: the Chinese HealthNER corpus (Lee and Lu, 2021) was used for both the FT and SM genres and the ROCLING-2022 CHNER dataset (Lee et al., 2022) was designed for the WA genre. For the FT genre, we have 23,008 sentences with a total of 1,109,918 characters, sourced from web-based health-related articles. The SM genre collected from medical question/answer forums includes 7,648 sentences with a total of 403,570 characters. The quantity in the FT genre about 3 times than that in the SM genre in the Chinese HealthNER corpus. After manual annotation, this corpus consists of 68,460 named entities across 10 defined entity types, of which 42,070 entities (about 61%) came from the FT genre and the remaining 26,390 entities belong to the SM genre. The training instances for the WA genre originate from the ROCLING 2022 CHNER dataset, which includes 3,205 sentences with a total of 118,116 characters and 13,369 named entities.
We use the existing named entities in the Chinese HealthNER corpus as the query terms to identify corresponding texts written in different genres.Our constructed test set includes 2,035/2,208/2,381 sentences respectively for the FT/SM/WA genres, resulting in a total of 340,091 characters and 28,896 named entities.
 
Table 2 presents detailed statistics for the mutually exclusive training and test sets, showing similar entity type distributions. The most frequently occurring type was Body, followed by Symptom, Disease and Chemical regardless of genre. In the training sets, these 4 types collectively accounted for about 82.9% of all named entity instances, with the remaining 6 types accounting for 17.1%. In the test sets, these 4 types accounted for 81.2% of the total, with the other 6 types accounting for the remaining 18.8%.

In the training set, sentences used for the FT and SM genres may or may not contain named entities, but sentences belonging to the WA genre contain at least one named entity. Each sentence had an average of 48.19 characters and 2.42 namedentities. For system performance evaluation, at least 2,000 sentences per genre were tested, each with an average of 51.34 characters and 4.36 named entities. The average sentence length in the test set was slightly longer and the named entity density was relatively higher than those in the training set.  

<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow" colspan="2">Datasets</th>
    <th class="tg-c3ow" colspan="3">Training Sets</th>
    <th class="tg-baqh" colspan="3">Test Sets</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow" colspan="2">Source</td>
    <td class="tg-c3ow" colspan="2">Chinese HealthNER<br>Corpus</td>
    <td class="tg-baqh">ROCLING 2022<br>CHNER Dataset</td>
    <td class="tg-baqh" colspan="3">ROCLING 2023<br>MultiNER-Health Datasets</td>
  </tr>
  <tr>
    <td class="tg-c3ow" colspan="2">Genre</td>
    <td class="tg-c3ow">FT</td>
    <td class="tg-baqh">SM</td>
    <td class="tg-baqh">WA</td>
    <td class="tg-baqh">FT</td>
    <td class="tg-c3ow">SM</td>
    <td class="tg-c3ow">WA</td>
  </tr>
  <tr>
    <td class="tg-c3ow" colspan="2">#Sentence</td>
    <td class="tg-c3ow">23,008</td>
    <td class="tg-baqh">7,648</td>
    <td class="tg-baqh">3,205</td>
    <td class="tg-baqh">2,035</td>
    <td class="tg-c3ow">2,208</td>
    <td class="tg-c3ow">2,381</td>
  </tr>
  <tr>
    <td class="tg-baqh" colspan="2">#Character</td>
    <td class="tg-baqh">1,109,918</td>
    <td class="tg-baqh">403,570</td>
    <td class="tg-baqh">118,116</td>
    <td class="tg-baqh">149,276</td>
    <td class="tg-baqh">98,317</td>
    <td class="tg-baqh">92,498</td>
  </tr>
  <tr>
    <td class="tg-baqh" colspan="2">#Named Entity</td>
    <td class="tg-baqh">42,070</td>
    <td class="tg-baqh">26,390</td>
    <td class="tg-baqh">13,369</td>
    <td class="tg-baqh">10,845</td>
    <td class="tg-baqh">8,292</td>
    <td class="tg-baqh">9,761</td>
  </tr>
  <tr>
    <td class="tg-baqh" rowspan="10">Entity<br>Type</td>
    <td class="tg-baqh">Body</td>
    <td class="tg-baqh">17,639</td>
    <td class="tg-baqh">8,772</td>
    <td class="tg-baqh">5,315</td>
    <td class="tg-baqh">2,461</td>
    <td class="tg-baqh">2,572</td>
    <td class="tg-baqh">3,843</td>
  </tr>
  <tr>
    <td class="tg-baqh">Symptom</td>
    <td class="tg-baqh">6,432</td>
    <td class="tg-baqh">6,472</td>
    <td class="tg-baqh">1,944</td>
    <td class="tg-baqh">2,635</td>
    <td class="tg-baqh">2,280</td>
    <td class="tg-baqh">1,890</td>
  </tr>
  <tr>
    <td class="tg-baqh">Instrumrent</td>
    <td class="tg-baqh">743</td>
    <td class="tg-baqh">346</td>
    <td class="tg-baqh">250</td>
    <td class="tg-baqh">190</td>
    <td class="tg-baqh">41</td>
    <td class="tg-baqh">149</td>
  </tr>
  <tr>
    <td class="tg-baqh">Examination</td>
    <td class="tg-baqh">444</td>
    <td class="tg-baqh">2,178</td>
    <td class="tg-baqh">207</td>
    <td class="tg-baqh">223</td>
    <td class="tg-baqh">511</td>
    <td class="tg-baqh">180</td>
  </tr>
  <tr>
    <td class="tg-baqh">Chemical</td>
    <td class="tg-baqh">5,716</td>
    <td class="tg-baqh">1,118<br></td>
    <td class="tg-baqh">1,718</td>
    <td class="tg-baqh">1,124</td>
    <td class="tg-baqh">321</td>
    <td class="tg-baqh">748</td>
  </tr>
  <tr>
    <td class="tg-baqh">Disease</td>
    <td class="tg-baqh">5,865</td>
    <td class="tg-baqh">4,214</td>
    <td class="tg-baqh">2,609</td>
    <td class="tg-baqh">2,300</td>
    <td class="tg-baqh">1,322</td>
    <td class="tg-baqh">1,970</td>
  </tr>
  <tr>
    <td class="tg-baqh">Drug</td>
    <td class="tg-baqh">1,165</td>
    <td class="tg-baqh">1,060</td>
    <td class="tg-baqh">481</td>
    <td class="tg-baqh">932</td>
    <td class="tg-baqh">746</td>
    <td class="tg-baqh">451</td>
  </tr>
  <tr>
    <td class="tg-baqh">Supplement</td>
    <td class="tg-baqh">1,338</td>
    <td class="tg-baqh">187</td>
    <td class="tg-baqh">183</td>
    <td class="tg-baqh">47</td>
    <td class="tg-baqh">92</td>
    <td class="tg-baqh">56</td>
  </tr>
  <tr>
    <td class="tg-baqh">Treatment</td>
    <td class="tg-baqh">2,031</td>
    <td class="tg-baqh">1,077</td>
    <td class="tg-baqh">468</td>
    <td class="tg-baqh">512</td>
    <td class="tg-baqh">363</td>
    <td class="tg-baqh">308</td>
  </tr>
  <tr>
    <td class="tg-baqh">Time</td>
    <td class="tg-baqh">697</td>
    <td class="tg-baqh">966</td>
    <td class="tg-baqh">194</td>
    <td class="tg-baqh">421</td>
    <td class="tg-baqh">44</td>
    <td class="tg-baqh">166</td>
  </tr>
</tbody>
</table>
  
<p align="center">Table 3: Detailed data statistics.</p>

We hope the data sets collected and annotated for this shared task can facilitate and expedite future development of Chinese NER in the healthcare domain. Therefore, the gold standard test set and evaluation scripts are made publicly available in GitHub repositories as follows: 

* Chinese HealthNER Corpus (train, for FT/SM genre)  
<a href="https://github.com/NYCU-NLPLab/Chinese-HealthNER-Corpus" target="_blank">https://github.com/NYCU-NLPLab/Chinese-HealthNER-Corpus</a>
* ROCLING-2022 Shared Task (train, for WA genre)  
<a href="https://github.com/NYCU-NLPLab/ROCLING-2022-ST-CHNER" target="_blank">https://github.com/NYCU-NLPLab/ROCLING-2022-ST-CHNER</a>
* ROCLING-2023 Shared Task (test, this repository)  
<a href="https://github.com/NYCU-NLPLab/ROCLING-2023-ST-MultiNERHealth" target="_blank">https://github.com/NYCU-NLPLab/ROCLING-2023-ST-MultiNERHealth</a> 


# Evaluation
Performance is evaluated by examining the difference between the machine-predicted and human-annotated BIO tags. Standard precision, recall and F1-score are the most typical evaluation metrics of NER systems at a character level, and are used here. If the predicted tag of a character in terms of BIO format was completely identical with the gold standard, the character in the testing instances was regarded as correctly recognized.Precision is defined as the percentage of named entities found by the NER system that are correct. Recall is the percentage of named entities present in the test set found by the NER system. The F1-score is the harmonic mean of precision and recall.

```bash
#Place the prediction files in the Input folder. The prediction file should be named as "WA_result.txt", "SM_result.txt", and "FT_result.txt".
#It will generate the corresponding "WA_result_Eval.txt", "SM_result_Eval.txt", and "FT_result_Eval.txt" in the Eval folder.
python turn_to_eval.py

#It will generate the "WA_result_Score.txt", "SM_result_Score.txt", and "FT_result_Score.txt" in the Score folder.
python conlleval.py

#It will generate the "Overall_Score.txt" in the Score folder.
python socre.py
```
# Results
The policy of this shared task is an open test. Participating systems are allowed to use other publicly available data for this shared task, but the usage should be specified in their system description paper. Each team was allowed to provide at most three submissions during the evaluation period. Among eight registered teams, six submitted their testing results, providing a total of 16 submissions, from which the submission with the best macro-averaging F1-score of each team was kept for official performance ranking. 
|  Rank  |  Team  |  Formal texts <br>F1-score (%)  |  Social media <br>F1-score (%)  |  Wikipedia <br>F1-score (%)  |  Macro-averaging <br>F1-score (%)  |
|  :----:  | ----  | ----  |  ----  |  ----  |  ----  |
|  1  |  **crowNER** (Wang et al., 2023)  |  65.49  |  69.54  |  73.63  |  69.55  |
|  2  |  **YNU-HPCC** (Pang et al., 2023) |  61.96  |  71.11  |  72.13  |  68.40  |
|  3  |  **ISLab** (Wu et al., 2023) |  62.52  |  71.42  |  71.19  |  68.38  |
|  4  |  **SCU-MESCLab** (Luo et al., 2023) |  62.51  |  71.33  |  70.57  |  68.14  |
|  5  |  **YNU-ISE-ZXW** (Zhang et al., 2023) |  62.79  |  70.22  |  70.37  |  67.79  |
|  6  |  **LingX** (Wang et al., 2023)  |  51.23  |  59.28  |  60.54  |  57.02  |

# Citation
Please cite the following paper for ROCLING 2023 MultiNER-Health Datasets:

Lung-Hao Lee, Tzu-Mi Lin, and Chao-Yi Chen. 2023. Overview of the ROCLING 2023 Shared Task for Chinese Multi-genre Named Entity Recognition in the Healthcare Domain. In *Proceedings of the 35th Conference on Computational Linguistics and Speech Processing*, pp. 333-338.

@article{ROCLING 2023,  
author={Lung-Hao Lee, Tzu-Mi Lin, and Chao-Yi Chen},  
title={Overview of the ROCLING 2023 Shared Task for Chinese Multi-genre Named Entity Recognition in the Healthcare Domain},  
year={2023},  
conference={In Proceedings of the 35th Conference on Computational Linguistics and Speech Processing},  
pages={333-338}  
}

# References
Lung-Hao Lee, and Yi Lu. 2021. Multiple embeddings enhanced multi-graph neural networks for Chinese healthcare named entity recognition. *IEEE Journal of Biomedical and Health Informatics*, 25(7): 2801-2810.  

Lung-Hao Lee, Chao-Yi Chen, Liang-Chih Yu, and Yuen-Hsien Tseng. 2022. Overview of the ROCLING 2022 shared task for Chinese healthcare named entity recognition. In *Proceedings of the 34th Conference on Computational Linguistics and Speech Processing*, pp. 363-368.
 
Yin-Chieh Wang, Wen-Hong Wu, Feng-Yu Kuo, Han- Chun Wu, Te-Yu Chi, Te-Lun Yang, Sheh Chen, and Jyh-Shing Roger Jang. 2023. CrowNER at ROCLING 2023 MultiNER-Health Task: enhancing NER task with GPT paraphrase augmentation on sparsely labeled data. In *Proceedings of the 35th Conference on Computational Linguistics and Speech Processing*, pp. 339-349.
  
Chonglin Pang, You Zhang, and Xiaobing Zhou. YUN- HPCC at ROCLING 2023 MultiNER-Health Task: a transformer-based approach for Chinese healthcare NER. In  *Proceedings of the 35th Conference on Computational Linguistics and Speech Processing*, pp. 317-324.

Jun-Jie Wu, Tao-Hsing Chang, and Fu-Yuan Hsu. 2023. ISLab at ROCLING 2023 MultiNER-Health Task: a three-stage NER model combining textual content and label semantics. In *Proceedings of the 35th Conference on Computational Linguistics and Speech Processing*, pp. 359-366.

Tzu-En Su, Ruei-Cyuan Su, Ming-Hsiang Su, and Tsung-Hsien Yang. 2023. 2023. SCU-MESCLab at ROCLING-2023 Shared Task: Named Entity Recognition Using Multiple Classifier Model. In *Proceedings of the 35th Conference on Computational Linguistics and Speech Processing*, pp. 311-316.

Xingwei Zhang, Jin Wang, and Xuejie Zhang. 2023. YUN-ISE-ZXW at ROCLING 2023 MultiNER- Health Task: a transformer-based model with LoRA for Chinese healthcare named entity recognition. In *Proceedings of the 35th Conference on Computational Linguistics and Speech Processing*, pp. 325-332.

Xuelin Wang and Qihao Yang. 2023. LingX at ROCLING 2023 MultiNER-Health Task: intelligent capture of Chinese medical named entities by LLMs. In *Proceedings of the 35th Conference on Computational Linguistics and Speech Processing*, pp. 350-358.
