title: Lessons from Statistical Consulting
date: 2020-03-16
published: 2020-03-16
abstract: After a quarter of offering my services as a statistical consultant to researchers around Stanford, I began to see patterns I didn't expect.
tag: [statistics, consulting, writing]



The Stanford Statistics department offers a unique service; any and all researchers from across the university can come discuss their ideas with Master's and PhD students. Eager to see whether I could apply my coursework to actual questions of experimental design, inference, and prediction, I signed up to be a consultant for the quarter. The experience was as challenging as I had expected, but the difficulty did not stem from choosing the best model or interpreting p-values. In fact, most cases presented problems that were not actually "statistics questions," but instead required a conversation about research goals and assumptions.

I spoke with students and professors working in medicine, biology, law, business, political science, and psychology, but they shared quite similar questions and concerns. Certainly some clients came in with difficult queries about experimental design, multi-level modeling, and valid inference (and had me quickly reaching for a textbook before attempting an answer). However, for most clients, I found that I could be much more helpful with a few probing questions instead of simply explaining how to fit a regression. Below I outline the most common misunderstandings and my efforts to work through them.

&nbsp;&nbsp;
### 3. The Streetlight Effect
&nbsp;

The old joke goes that the drunkard looks for his missing keys under the streetlight, not because that is where he lost them, but because that's where the light is. In a similar manner, some researchers start with a dataset and then try to formulate questions that might be answered using only this data. In principle, this may seem like a perfectly fine approach, but so often it leads to a tunnel vision in which one fails to ask whether the questions asked are interesting to the field or whether there are too many confounders and sources of variation outside this dataset to have any confidence in the findings.

&nbsp;

For example, imagine you have found an exciting dataset published by the World Health Organization with some binary indicators describing various countries' healthcare systems and their rates of heart disease. You might start down the path by thinking a regression could be a great model here, demonstrating how different features of a healthcare system affect actual health outcomes. Yet there are many problems to this  approach. Health outcomes depend on much than the structure of a healthcare system, and by looking across the globe there is no reasonable assumption that you are looking at populations with similar diets, lifestyles, and access to medicines. By looking at a single time period, we cannot perform a causal analysis and may even measure a relationship that works in the opposite causal direction.

&nbsp;

The found dataset may help inspire questions to research, but once those questions are formed the researcher should consider what information would be optimal and whether it may be reasonable to acquire it. They could consider looking for natural experiments to answer causal questions and those that might be most interesting to the subject matter experts they hope would read their work. In the end, these students didn't need statistics help but instead needed to reconsider their process and design.

&nbsp;&nbsp;

### 2. Data Without a Plan
&nbsp;

"Far better an approximate answer to the *right* question, which is often vague, than an *exact* answer to the wrong question, which can always be made precise."

-John Tukey, *The Future of Data Analysis*

&nbsp;

Thousands of protein levels in hundreds of cultures from 10 mice at 5 time periods. Five CT scans from 100 patients with four randomized treatments. Experiments are a lot of work; they often involve live animals or people and multiple measurements and time periods. If you embark on a study without defining a specific, data-oriented question you seek to answer as well as the statistical method you plan to use, there is a high chance you end up with a mess.

&nbsp;

Let's say you wish to measure variation across individuals. If you take many observations on a cellular level from 3 mice, you still only have 3 individuals. Your dataset looks large, but if you cannot assume those cell samples are independent from one another, you will have little to say about how variation affect individual outcomes. Alternatively, perhaps you collected the necessary data, but your study design has some features of a repeated measures ANOVA but also uses multi-level modelling and you want to make comparisons within and across levels and time periods. Structuring your study to fit into specific, well-tested models that rely on valid assumptions for your data will make your analysis much easier and your results more convincing.

&nbsp;

It is easy to convince yourself that you have a plan. You have a general question that seems answerable with your current experiment design. Sit down at your computer and try to code your analysis with some simulated data. If you cannot translate your idea into code now, your study design might be in trouble.

&nbsp;&nbsp;

### 1. Asking Too Much of Statistics

&nbsp;

On a good day, statistics can give an answer to the questions "how much?" and "with what certainty?" I say on a good day since we need the assumptions of any model to be at least somewhat valid to get these results, but for now let's imagine they hold. As a researcher, your paramount objective should be how your work will fit into the current work in your field and how it will add to our understanding.

&nbsp;

You may have a large number of datapoints, perfectly normal, homoskedastic errors, and your regression may have spot on estimates of predictor coefficients. But if what you really needed was a causal model, the statistics won't help you here. Conversely, if you have a small number of datapoints that show an important effect in your field, don't let your inability to get a 0.05 p-value stop you from writing a great paper and gathering support to collect more data.

&nbsp;

In the end, statistics is a powerful tool for extrapolation, but it is up to the researcher to match the methods with a reasonable theory, careful research design, and orthoganlize their treatments.
