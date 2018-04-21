# Surname Identifier
## Trying to discern surname origin using k-NN in Python

A while ago I had a dream where I was using k-NN to determine the ethnicity of
people's surnames using [Levenshtein
distance](https://en.wikipedia.org/wiki/Levenshtein_distance). Here is the
realization of that dream.

I used the [surname database](https://surnames.behindthename.com) from the
website [Behind the Name](https://www.behindthename.com) to achieve this goal.
It is far from a perfect database and I had to do a lot of editing to get
workable data for k-NN. Some categories were simply too small to be considered
for inclusion. Some categories are multi-ethnic and so would likely not allow
reliable distinctions in edit distance as linguistic differences can be huge.
The [African](https://surnames.behindthename.com/names/usage/african) category
is exceptional in this regard: not only is it very small but the surnames run
the gamut from West and East African ethnic groups to the foreign Afrikaaner
settlers! Some names are not particular to any one ethnic group and so would
provide little information to the classifier. There were indeed numerous names
shared by the English and the Celtic ethnic groups of the British Isles with
identical spelling but completely different etymologies! And the database is
not at all comprehensive. It includes only the following ethnic groups:

* Arabic
* Armenian
* Bulgarian
* Chinese
* Czech-Slovak
* Dano-Norwegian
* Dutch
* English
* Finnish
* French
* German
* Greek
* Hungarian
* Irish
* Italian
* Japanese
* Polish
* Portuguese
* Romanian
* Russian
* Scottish
* Serbo-Croatian
* Spanish
* Swedish
* Welsh

This selection falls well short of the true ethnic diversity of the world. And
the situation is exacerbated by the fact that some ethnic groups are
represented far better than others. For example, there are only 23 Greek
surnames, included only because of how distinctively Greek they sound,
something I figured would count a lot given the distance metric being used. On
the other hand, English surnames dwarf all other categories—even after I had to
throw many out—with 1,151 members. The data I have certainly leave a lot to be
desired.

Nonetheless I pressed on. Eventually I came up with a completed database
scrubbed of any duplicate names or other imperfections. All surnames were
lowercased to simply handling. Diacritical marks were also scrubbed using the
excellent Python module [Unidecode](https://pypi.org/project/Unidecode/). The
presence of diacritical marks would give many human competitors an advantage
but I was concerned about making things too easy for the classifier.

When all was said and done I ran into another problem. scikit-learn, the
machine learning framework that the dream said I was using to classify the
surnames only supports the use of numerical data with k-NN, even if a custom
distance metric is used. Oh well, so much for my dream. Fortunately, I was at
least able to use scikit-learn to get a stratified sample of the data and,
because at least a naïve implementation of k-NN is relatively easy to
write—and naïve worked here—I had my own implementation up and running pretty
soon. It can be run with `python3 identify.py`, which will spit out a report
comparing predictions about the test set with actual ethnicities and
concluding with an overall accuracy score.

The results are impressive and unimpressive at the same time. With the rule of
thumb of *k* = 5, which really does appear to be about the best, the accuracy
of the classifier hovers somewhere around 60%. This is much less than the
near-total accuracy of the best machine learning classifiers. But it's also
much more than the probability of success with random guessing, which, by the
calculations available in `random-guessing.py`, is about 10.6%. A sixfold
improvement over random chance with a deeply suboptimal database is
encouraging and suggests that accuracy could be improved considerably with
more data. I have also considered excluding ethnic groups with few names and
focusing only on those with, say, one hundred or more members each to see if
that would improve performance. (**EDIT:** the branch reduced of this
repository shows what happens when only ethnic groups with two hundred or more
surnames are included. The accuracy increases to above 70%, though the
advantage over random guessing is diminished: random guessing is now effective
over 20% of the time.)
