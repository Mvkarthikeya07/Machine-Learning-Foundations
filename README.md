# 🜲 Machine Learning Foundations

> *Anyone can `import` a model. Few bother to understand what it does before they call `.fit()`.*

This repository is a deliberate, line-by-line dissection of the algorithms most engineers treat as black boxes. No shortcuts, no "trust the library" hand-waving — every project here exists to interrogate a single concept until it's understood at the level of geometry, probability, and code, not just API syntax.

If you're looking for a polished SaaS product, look elsewhere. If you want proof that someone has actually sat down and worked out *why* a decision tree splits where it splits, *why* PCA's eigenvectors are the axes that matter, and *why* a Markov chain's hidden states behave the way they do — you're in the right place.

---

## Doctrine

1. **Derive before you import.** Library calls only happen after the underlying math is understood well enough to argue with it.
2. **Visualize or it didn't happen.** If a result can't be plotted, drawn, or printed in a way that proves it worked, it isn't finished.
3. **Small, sharp, reproducible.** Every project is a self-contained `main.py` — no hidden state, no unnecessary scaffolding, nothing to configure before it runs.

---

## The Archive

| # | Project | Domain | Core Idea |
|---|---------|--------|-----------|
| 01 | [`CART`](./CART-learning-algorithms-to-perform-categorization.-main) | Supervised Learning | Decision tree classification via Gini-driven recursive splitting on the Iris dataset, with full tree visualization |
| 02 | [`Ensemble Learning`](./Ensemble-learning-main) | Supervised Learning | Random Forest vs. AdaBoost — comparing bagging and boosting head-to-head, with PCA-reduced decision-boundary plots |
| 03 | [`Hierarchical Clustering`](./Hierachial-clustering-main) | Unsupervised Learning | Agglomerative clustering implemented from raw Euclidean distance up — no `sklearn.cluster` shortcuts |
| 04 | [`Principal Component Analysis`](./Principal-Component-Analysis-main) | Dimensionality Reduction | Variance-preserving feature transformation on the Wine dataset, with a before/after classifier accuracy comparison |
| 05 | [`Hidden Markov Model`](./Hidden-markov-model-main) | Probabilistic Modeling | Transition and emission matrices driving inference over hidden states from observed sequences |
| 06 | [`ML Basics`](./ML_basics_exp1-main) | Foundations | The unglamorous reps — factorials, palindromes, primes, digit sums — because algorithmic fluency starts with the boring stuff done right |
| 07 | [`Expense Calculator`](./Expense-calculator-main) | Applied Engineering | A Tkinter GUI with CSV persistence and Matplotlib breakdowns — proof the fundamentals extend past notebooks into real interfaces |
| 08 | [`Student Score Prediction`](./Student-Score-Prediction-main) | Regression *(reserved)* | Slot reserved for a regression-based score predictor — not yet built |

---

## Stack

`Python` · `NumPy` · `scikit-learn` · `hmmlearn` · `Matplotlib` · `Tkinter`

No frameworks doing the thinking. The math is the dependency.

---

## Why This Exists

These aren't tutorial-follow-alongs left to rot in a repo. Each one was built to answer a question that "just use the library" doesn't actually answer: *what is the model doing, mechanically, between input and output?* That question is the entire curriculum here.

This is a learning archive — not production code, not a portfolio piece pretending otherwise. It's kept public because understanding earned the hard way is worth showing.
