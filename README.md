# Poetic Machines

MA/MFA Computational Arts at Goldsmiths College, by [*Iris Colomb*](https://iriscolomb.com/) and [*Jérémie Wenger*](https://jeremiewenger.com/)

---

Language and textuality are one of the fundamental and most exciting domains of human expression, in the arts and beyond. Practitioners of all kinds (writers of course, but also performers, musicians, visual artists, film makers, game designers, etc.) engage with language in their practices. What is more, one of the defining technological advances of our time, Large Language Models, was achieved by applying machine learning techniques to textual corpora.

In this course, students will build foundational knowledge and command of programming concepts (variables, conditionals, functions, loops, data structures, etc.) with a special emphasis on text and language. This will involve learning how to handle language using programming (using Python and JavaScript), developing abilities to build creative pipelines and/work visually with text, as well as experimenting with chat interfaces, as well as various LLM concepts and techniques (prompting, word embeddings, fine-tuning).

The creative side of the course will draw inspiration from various movements, including the Oulipo (Ouvroir de Littérature Potentielle, combining writing and constrained procedures); Visual Poetry (including Visual and Artistic works using text); Concrete Poetry; Conceptual Writing, as well as works using found/existing text. Throughout the term we will create small prototypes applying creative constraints involving various methods through the use of Python/p5.js as well as applying algorithmic thinking to creative processes using only pen and paper. Experiments in the students’ native tongue, as well as multilingual ones, will be encouraged!

This course is open to those who feel comfortable with writing as well as those who usually avoid it. Students will be free to choose to use their own writing, to work from existing materials (including literary works, articles, instruction manuals, tweets, slogans, logos, etc.), or experiment with the synthetic output of LLMs.

*Poetic Machines* hopes to encourage opening up the creative possibilities of working between and beyond languages, from producing multilingual pieces to treating text as image and image as text.

## Installation

The recommended tech stack for this course is to use [miniforge](https://github.com/conda-forge/miniforge?tab=readme-ov-file#install), which is an optimised, more lightweight version of [Anaconda](https://www.anaconda.com).

Once you have miniforge installed, you can create an environment with this command (you need to be in the `poetic.machines` directory!
```bash
mamba create -f environment.yaml
```

Once this is done, you can activate your environment like so:

```bash
conda activate poetic.machines
```

(You can use `conda deactivate` to turn it off.)

To test that your environment works as it shoud, you can do:

```bash
which pip # on Linux/MacOS
where pip # on Windows
```

And there should be a file path that has `miniforge/base/envs/poetic.machines/` in it.

**Note**: this is equivalent to:

```bash
mamba create -n poetic.machines python==3.12
conda activate poetic.machines
# now your terminal should display the env name like so:
# (poetic.machines) $ 
pip install -r requirements.txt
```

### Working on Colab

When using [Google Colab](https://colab.research.google.com/) you will need to use the following cell to install `py5canvas` (based on [this](https://github.com/pygobject/pycairo/issues/39#issuecomment-391830334))

```python
!apt-get install libcairo2-dev libjpeg-dev libgif-dev
!pip install py5canvas
```

## References: Learning Programming / Creative Coding

- Dan Shiffman, ITP, [Creative Coding for Beginners](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6Zy51Q-x9tMWIv9cueOFTFA) (JavaScript)
- Dan Shiffman, ITP, [Programming with Text](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6YrbSJBg32eTzUU50E2B8Ch) (JavaScript)
- Dan Shiffman, ITP, [Workflow: Terminal, Shell, Node.js, VSCode](https://www.youtube.com/watch?v=46WOuOrMwTQ)
- Dan Shiffman, ITP, [Git and Github for Poets](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6ZF9C0YMKuns9sLDzK6zoiV)
- Allison Parrish, ITP, [Reading and Writing Electronic Text](https://rwet.decontextualize.com/) (and [more!](https://www.decontextualize.com/))
- Ana Bell, MIT, [Introduction to CS and Programming Using Python](https://www.youtube.com/playlist?list=PLUl4u3cNGP62A-ynp6v6-LGBCzeH3VAQB), comprehensive CS course with Python

## References: maths

Working with programming suddenly brings back maths and logic as things that are really useful for understanding and making things (since they allow you precisely to describe behaviours or phenomena). It's never too late to start learning, and current resources are better than ever before! Here are a few recommendations, that can become quite useful when needing to refresh a particular subject:

- [Grant Sanderson, aka 3Blue1Brown](https://www.youtube.com/3blue1brown)
- [Eddie Woo](https://www.youtube.com/@misterwootube)
- [Khan Academy](https://www.youtube.com/@khanacademy)
