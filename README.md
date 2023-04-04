# Text Analysis of Dream of Red Mansions

## 1.Content

1. Write the module to realize the frequency statistics function of a given word or word in Chinese text;
(1) Data cleaning, use zhconv.convert to convert traditional characters in the text into simplified characters, and then use the find_chinese function written by yourself to filter out non-Chinese characters, and please wash the data after completion.
(2) Utilize the Getlist function written to make the user input the words that the user wants to query the word frequency, and then obtain all the word frequencies of the text passed into the function by calling Getcount, and then output the word frequency of the words that the user wants to see.
2. Use the function module in (1) to analyze the word frequency of the common empty and full words in the file "dreamofredmaison.txt" in the first 80 chapters and the last 40 chapters, and save the analysis results in the text file;
(1) First use the Break function to divide the text into the first 80 chapters and the last 40 chapters, then set commonly used function words and content words, and put them in the list.
(2) After obtaining the frequencies of commonly used function words in the first 80 chapters, commonly used content words in the first 80 chapters, commonly used function words in the last 40 chapters, and common content words in the last 40 chapters, store them in corresponding files respectively.
3. Use Matplotlib to visualize the analysis results in (2);
(1) Make two histograms based on commonly used function words and their corresponding first 80 chapters and last 40 chapters, and then make two histograms based on commonly used content words and their corresponding first 80 chapters and last 40 chapters.
(2) Make two cloud maps based on commonly used function words and their corresponding first eighty chapters and last forty chapters, and then make two cloud maps based on commonly used content words and their corresponding first eighty chapters and last forty chapters.
4. Use the GUI to compile the user interface, provide users with an interactive interface for selecting virtual and real words in classical Chinese, use the function in (1) to realize frequency statistics according to the user's choice, and dynamically present the analysis results realized in (3) to the user.
(1) First use QTdesigner to design a main window, the main window has two buttons, one of which is connected to the page for selecting content words, and the other button is connected to the page for selecting function words.
(2) Design a sub-window for selecting function words, providing check boxes for 18 function words commonly used, and the submit button is connected to another sub-window.
(3) Design a sub-window for filling in the content words, design a text box for users to input the content words they want to query, and two buttons on the right, one button is used to clear the text box, and the other button is used to submit. The submit button is connected to the same child window as the button in (2).
(4) Create sub-windows, design two GroupBoxes, and generate corresponding cloud graphs and histograms in these two places according to the selected or input words.

1.写模块实现中文文本中给定字或词的频率统计功能；

(1)数据清洗，利用zhconv.convert将文本中繁体字转化为简体字，然后利用自己编写的find_chinese函数过滤掉不是中文的字符，完成数据请洗。

(2)利用编写的Getlist函数使用户输入想要查询词频的字词，然后通过调用Getcount获得传入该函数的文本所有的词频，然后将用户想要看到的字词的词频输出。

2.运用（1）中功能模块分析文件“dreamofredmaison.txt”中前 80 回和后 40 回中常见文言虚实词的词频，分析结果存入文本文件；

(1)首先利用Break函数将文本分成前80回和后40回，然后设置常用的虚词和实词，将他们放在列表中。

(2)得到前八十回常用虚词、前八十回常用实词、后四十回常用虚词、后四十回常用实词的频率后将他们分别存入对应的文档中。

3.采用 Matplotlib 可视化（2）中的分析结果；

(1)根据常用虚词和其对应的前八十回后四十回做出两张柱状图，再根据常用实词和其对应的前八十回后四十回再做出两张柱状图。

(2)根据常用虚词和其对应的前八十回后四十回做出两张云图，再根据常用实词和其对应的前八十回后四十回再做出两张云图。

4.运用 GUI 编制用户界面，为用户提供选择文言虚实字词的交互界面，按照用户选择采用（1）中功能实现频率统计，并且把（3）中实现的分析结果动态呈现给用户。 

(1)首先用QTdesigner设计一个主窗口，主窗口有两个按钮，其中一个按钮连接选择实词的页面，另一个按钮连接选择虚词的页面。

(2)设计选择虚词的子窗口，提供了常用的18个虚词的复选框，提交按钮连接到另一个子窗口。

(3)设计填写实词的子窗口，设计文本框供用户输入想要查询的实词，右边两个按钮，一个按钮用来清空文本框，另一个按钮用来提交。提交按钮和（2）中按钮一样连接着相同的子窗口。

(4)建立子窗口，设计两个GroupBox，在这两个地方根据所选择或输入的词语生成相应的云图和柱状图。



## 2.Design Show

Just run Buser.py.

![image-20230404174112838](C:\Users\dell\AppData\Roaming\Typora\typora-user-images\image-20230404174112838.png)

The interface after selecting function words:

![image-20230404174346034](C:\Users\dell\AppData\Roaming\Typora\typora-user-images\image-20230404174346034.png)

choose some words:

![image-20230404174556352](C:\Users\dell\AppData\Roaming\Typora\typora-user-images\image-20230404174556352.png)

The interface after selecting content words:

![image-20230404174707010](C:\Users\dell\AppData\Roaming\Typora\typora-user-images\image-20230404174707010.png)

Enter some content words, remember to separate them with spaces!

![image-20230404174827884](C:\Users\dell\AppData\Roaming\Typora\typora-user-images\image-20230404174827884.png)