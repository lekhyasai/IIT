{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Copy of WORD@VEC",
      "provenance": [],
      "collapsed_sections": [],
      "toc_visible": true,
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/lekhyasai/IIT/blob/master/Copy_of_WORD_VEC.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "J-No6lRk5b6C",
        "colab_type": "text"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2YaIrAmb2AGo",
        "colab_type": "code",
        "outputId": "d3f4b701-bb3d-4c08-a87a-a17bbc9165ad",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        }
      },
      "source": [
        "import gensim\n",
        "import pandas as pd\n",
        "import nltk\n",
        "from nltk.corpus import brown\n",
        "nltk.download('brown')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[nltk_data] Downloading package brown to /root/nltk_data...\n",
            "[nltk_data]   Package brown is already up-to-date!\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8ejEJvrQPvCp",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "data=pd.read_csv('brown.csv')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "C3Ckfxk6P_ry",
        "colab_type": "code",
        "outputId": "67e059ea-978b-4b01-9a0c-d75cbf69885f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 289
        }
      },
      "source": [
        "data.head()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>filename</th>\n",
              "      <th>para_id</th>\n",
              "      <th>sent_id</th>\n",
              "      <th>raw_text</th>\n",
              "      <th>tokenized_text</th>\n",
              "      <th>tokenized_pos</th>\n",
              "      <th>label</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>cd05</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>Furthermore/rb ,/, as/cs an/at encouragement/n...</td>\n",
              "      <td>Furthermore , as an encouragement to revisioni...</td>\n",
              "      <td>rb , cs at nn in nn nn , pps rb bez jj to vb c...</td>\n",
              "      <td>religion</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>cd05</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>The/at Unitarian/jj clergy/nns were/bed an/at ...</td>\n",
              "      <td>The Unitarian clergy were an exclusive club of...</td>\n",
              "      <td>at jj nns bed at jj nn in vbn nns -- cs at nn ...</td>\n",
              "      <td>religion</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>cd05</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>Ezra/np Stiles/np Gannett/np ,/, an/at honorab...</td>\n",
              "      <td>Ezra Stiles Gannett , an honorable representat...</td>\n",
              "      <td>np np np , at jj nn in at nn , vbd ppl rb in a...</td>\n",
              "      <td>religion</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>cd05</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Even/rb so/rb ,/, Gannett/np judiciously/rb ar...</td>\n",
              "      <td>Even so , Gannett judiciously argued , the Ass...</td>\n",
              "      <td>rb rb , np rb vbd , at nn-tl md rb vb cs np ``...</td>\n",
              "      <td>religion</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>cd05</td>\n",
              "      <td>0</td>\n",
              "      <td>4</td>\n",
              "      <td>We/ppss today/nr are/ber not/* entitled/vbn to...</td>\n",
              "      <td>We today are not entitled to excoriate honest ...</td>\n",
              "      <td>ppss nr ber * vbn to vb jj nns wps vbd np to b...</td>\n",
              "      <td>religion</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  filename  ...     label\n",
              "0     cd05  ...  religion\n",
              "1     cd05  ...  religion\n",
              "2     cd05  ...  religion\n",
              "3     cd05  ...  religion\n",
              "4     cd05  ...  religion\n",
              "\n",
              "[5 rows x 7 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yn5eteUN2NeK",
        "colab_type": "code",
        "outputId": "33f0780c-ce14-4a5d-b8f7-54a7ebc894c1",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        }
      },
      "source": [
        "sentences = brown.sents()\n",
        "model = gensim.models.Word2Vec(sentences, min_count=1)\n",
        "model.save('brown_model')\n",
        "print(\"Brown corpus model saved.\")"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "2019-08-09 16:35:09,742 : INFO : collecting all words and their counts\n",
            "2019-08-09 16:35:09,747 : INFO : PROGRESS: at sentence #0, processed 0 words, keeping 0 word types\n",
            "2019-08-09 16:35:10,351 : INFO : PROGRESS: at sentence #10000, processed 219770 words, keeping 23488 word types\n",
            "2019-08-09 16:35:10,892 : INFO : PROGRESS: at sentence #20000, processed 430477 words, keeping 34367 word types\n",
            "2019-08-09 16:35:11,477 : INFO : PROGRESS: at sentence #30000, processed 669056 words, keeping 42365 word types\n",
            "2019-08-09 16:35:12,010 : INFO : PROGRESS: at sentence #40000, processed 888291 words, keeping 49136 word types\n",
            "2019-08-09 16:35:12,442 : INFO : PROGRESS: at sentence #50000, processed 1039920 words, keeping 53024 word types\n",
            "2019-08-09 16:35:12,775 : INFO : collected 56057 word types from a corpus of 1161192 raw words and 57340 sentences\n",
            "2019-08-09 16:35:12,777 : INFO : Loading a fresh vocabulary\n",
            "2019-08-09 16:35:12,994 : INFO : effective_min_count=1 retains 56057 unique words (100% of original 56057, drops 0)\n",
            "2019-08-09 16:35:12,995 : INFO : effective_min_count=1 leaves 1161192 word corpus (100% of original 1161192, drops 0)\n",
            "2019-08-09 16:35:13,156 : INFO : deleting the raw counts dictionary of 56057 items\n",
            "2019-08-09 16:35:13,159 : INFO : sample=0.001 downsamples 38 most-common words\n",
            "2019-08-09 16:35:13,160 : INFO : downsampling leaves estimated 854152 word corpus (73.6% of prior 1161192)\n",
            "2019-08-09 16:35:13,333 : INFO : estimated required memory for 56057 words and 100 dimensions: 72874100 bytes\n",
            "2019-08-09 16:35:13,334 : INFO : resetting layer weights\n",
            "2019-08-09 16:35:14,049 : INFO : training model with 3 workers on 56057 vocabulary and 100 features, using sg=0 hs=0 sample=0.001 negative=5 window=5\n",
            "2019-08-09 16:35:15,064 : INFO : EPOCH 1 - PROGRESS: at 20.81% examples, 190497 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:16,065 : INFO : EPOCH 1 - PROGRESS: at 42.29% examples, 194147 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:17,067 : INFO : EPOCH 1 - PROGRESS: at 61.21% examples, 192781 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:18,097 : INFO : EPOCH 1 - PROGRESS: at 88.13% examples, 190874 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:18,527 : INFO : worker thread finished; awaiting finish of 2 more threads\n",
            "2019-08-09 16:35:18,538 : INFO : worker thread finished; awaiting finish of 1 more threads\n",
            "2019-08-09 16:35:18,543 : INFO : worker thread finished; awaiting finish of 0 more threads\n",
            "2019-08-09 16:35:18,544 : INFO : EPOCH - 1 : training on 1161192 raw words (853954 effective words) took 4.5s, 190273 effective words/s\n",
            "2019-08-09 16:35:19,585 : INFO : EPOCH 2 - PROGRESS: at 20.81% examples, 186004 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:20,614 : INFO : EPOCH 2 - PROGRESS: at 42.29% examples, 189327 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:21,618 : INFO : EPOCH 2 - PROGRESS: at 61.21% examples, 189446 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:22,639 : INFO : EPOCH 2 - PROGRESS: at 87.02% examples, 186970 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:23,120 : INFO : worker thread finished; awaiting finish of 2 more threads\n",
            "2019-08-09 16:35:23,128 : INFO : worker thread finished; awaiting finish of 1 more threads\n",
            "2019-08-09 16:35:23,136 : INFO : worker thread finished; awaiting finish of 0 more threads\n",
            "2019-08-09 16:35:23,137 : INFO : EPOCH - 2 : training on 1161192 raw words (854917 effective words) took 4.6s, 186376 effective words/s\n",
            "2019-08-09 16:35:24,179 : INFO : EPOCH 3 - PROGRESS: at 20.81% examples, 185043 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:25,198 : INFO : EPOCH 3 - PROGRESS: at 42.29% examples, 189513 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:26,229 : INFO : EPOCH 3 - PROGRESS: at 62.56% examples, 192604 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:27,231 : INFO : EPOCH 3 - PROGRESS: at 89.23% examples, 190247 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:27,632 : INFO : worker thread finished; awaiting finish of 2 more threads\n",
            "2019-08-09 16:35:27,644 : INFO : worker thread finished; awaiting finish of 1 more threads\n",
            "2019-08-09 16:35:27,645 : INFO : worker thread finished; awaiting finish of 0 more threads\n",
            "2019-08-09 16:35:27,647 : INFO : EPOCH - 3 : training on 1161192 raw words (853828 effective words) took 4.5s, 189421 effective words/s\n",
            "2019-08-09 16:35:28,655 : INFO : EPOCH 4 - PROGRESS: at 19.95% examples, 184477 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:29,657 : INFO : EPOCH 4 - PROGRESS: at 40.69% examples, 187325 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:30,665 : INFO : EPOCH 4 - PROGRESS: at 60.42% examples, 190269 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:31,669 : INFO : EPOCH 4 - PROGRESS: at 85.91% examples, 188322 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:32,195 : INFO : worker thread finished; awaiting finish of 2 more threads\n",
            "2019-08-09 16:35:32,207 : INFO : worker thread finished; awaiting finish of 1 more threads\n",
            "2019-08-09 16:35:32,209 : INFO : worker thread finished; awaiting finish of 0 more threads\n",
            "2019-08-09 16:35:32,210 : INFO : EPOCH - 4 : training on 1161192 raw words (853993 effective words) took 4.6s, 187389 effective words/s\n",
            "2019-08-09 16:35:33,223 : INFO : EPOCH 5 - PROGRESS: at 19.95% examples, 183906 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:34,224 : INFO : EPOCH 5 - PROGRESS: at 40.69% examples, 187262 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:35,235 : INFO : EPOCH 5 - PROGRESS: at 60.42% examples, 189985 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:36,275 : INFO : EPOCH 5 - PROGRESS: at 87.02% examples, 188346 words/s, in_qsize 0, out_qsize 0\n",
            "2019-08-09 16:35:36,758 : INFO : worker thread finished; awaiting finish of 2 more threads\n",
            "2019-08-09 16:35:36,770 : INFO : worker thread finished; awaiting finish of 1 more threads\n",
            "2019-08-09 16:35:36,772 : INFO : worker thread finished; awaiting finish of 0 more threads\n",
            "2019-08-09 16:35:36,773 : INFO : EPOCH - 5 : training on 1161192 raw words (854096 effective words) took 4.6s, 187498 effective words/s\n",
            "2019-08-09 16:35:36,775 : INFO : training on a 5805960 raw words (4270788 effective words) took 22.7s, 187937 effective words/s\n",
            "2019-08-09 16:35:36,776 : INFO : saving Word2Vec object under brown_model, separately None\n",
            "2019-08-09 16:35:36,778 : INFO : not storing attribute vectors_norm\n",
            "2019-08-09 16:35:36,780 : INFO : not storing attribute cum_table\n",
            "/usr/local/lib/python3.6/dist-packages/smart_open/smart_open_lib.py:398: UserWarning: This function is deprecated, use smart_open.open instead. See the migration notes for details: https://github.com/RaRe-Technologies/smart_open/blob/master/README.rst#migrating-to-the-new-open-function\n",
            "  'See the migration notes for details: %s' % _MIGRATION_NOTES_URL\n",
            "2019-08-09 16:35:37,529 : INFO : saved brown_model\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "Brown corpus model saved.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ibr5Kmam3C0I",
        "colab_type": "code",
        "outputId": "7dee5cfb-4670-4f4e-bd0e-b14f300ea3e6",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 292
        }
      },
      "source": [
        "model = gensim.models.Word2Vec.load('brown_model')\n",
        "#words most similar to mother\n",
        "print(model.most_similar('mother'))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "2019-08-09 16:36:06,227 : INFO : loading Word2Vec object from brown_model\n",
            "/usr/local/lib/python3.6/dist-packages/smart_open/smart_open_lib.py:398: UserWarning: This function is deprecated, use smart_open.open instead. See the migration notes for details: https://github.com/RaRe-Technologies/smart_open/blob/master/README.rst#migrating-to-the-new-open-function\n",
            "  'See the migration notes for details: %s' % _MIGRATION_NOTES_URL\n",
            "2019-08-09 16:36:06,803 : INFO : loading wv recursively from brown_model.wv.* with mmap=None\n",
            "2019-08-09 16:36:06,804 : INFO : setting ignored attribute vectors_norm to None\n",
            "2019-08-09 16:36:06,809 : INFO : loading vocabulary recursively from brown_model.vocabulary.* with mmap=None\n",
            "2019-08-09 16:36:06,813 : INFO : loading trainables recursively from brown_model.trainables.* with mmap=None\n",
            "2019-08-09 16:36:06,816 : INFO : setting ignored attribute cum_table to None\n",
            "2019-08-09 16:36:06,817 : INFO : loaded brown_model\n",
            "/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:3: DeprecationWarning: Call to deprecated `most_similar` (Method will be removed in 4.0.0, use self.wv.most_similar() instead).\n",
            "  This is separate from the ipykernel package so we can avoid doing imports until\n",
            "2019-08-09 16:36:06,951 : INFO : precomputing L2-norms of word weight vectors\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "[('father', 0.9835339784622192), ('husband', 0.965451717376709), ('wife', 0.9488356709480286), ('friend', 0.9331713914871216), ('son', 0.9253172874450684), ('eagle', 0.9185556769371033), ('nickname', 0.918049693107605), ('addiction', 0.9122201800346375), ('voice', 0.9024170637130737), ('patient', 0.8969205617904663)]\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/gensim/matutils.py:737: FutureWarning: Conversion of the second argument of issubdtype from `int` to `np.signedinteger` is deprecated. In future, it will be treated as `np.int64 == np.dtype(int).type`.\n",
            "  if np.issubdtype(vec.dtype, np.int):\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kWAYpbe1_ILj",
        "colab_type": "code",
        "outputId": "be9fef8f-d407-4793-dcff-6280d5eda116",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 360
        }
      },
      "source": [
        "print(model['human'])"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[ 0.37767145  0.9416834   0.14043489 -0.3091825  -0.36065924 -0.4708953\n",
            " -0.26416093  1.3189325  -0.44595125 -0.3706688  -0.8690762  -0.61706644\n",
            " -0.3033031   0.03470171  0.12185411 -0.23283377  1.1984245  -0.35633376\n",
            " -0.21573403 -0.3610968   0.85121596 -0.7704158   0.04728983 -0.38387814\n",
            " -0.8336495   0.3191297  -0.25304398 -1.2347447   0.40394184 -0.7414153\n",
            "  0.41094798 -1.1409808   0.97543013  0.22973564  0.7311361  -0.25181758\n",
            "  0.9995455   0.7205169   0.24499522  0.3503789  -0.09648871  0.4356911\n",
            " -0.61711305 -0.19074509  0.07956723 -0.30365682 -0.48418176 -0.40031713\n",
            "  0.07584447 -0.0832014   0.5421153  -0.59530675  0.266338    0.10296029\n",
            "  0.7048967   0.11504292  1.2632961   0.04097997 -0.3019295  -0.2270781\n",
            "  0.7210621   0.3738009  -0.07108223  0.37273735 -1.0140934   0.12266257\n",
            " -0.31784573 -0.30399442  0.7053341   0.14996871 -0.27130932 -0.41422436\n",
            " -0.25010127 -0.20231692 -0.02517646  0.80805933 -0.11950237  0.41479754\n",
            "  0.15836295  0.91844076  0.39456853 -0.532543   -1.4962904   0.45404318\n",
            " -1.0613315  -0.26569077  0.03657771 -0.60214967 -0.76991177  0.37042496\n",
            " -0.3757319   0.00748515  0.37713563  0.01966861  0.35111192  0.36461207\n",
            " -0.12181834 -0.12601672  0.4458669  -0.6864951 ]\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:1: DeprecationWarning: Call to deprecated `__getitem__` (Method will be removed in 4.0.0, use self.wv.__getitem__() instead).\n",
            "  \"\"\"Entry point for launching an IPython kernel.\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4W4Xx_4JQLTS",
        "colab_type": "code",
        "outputId": "3d086396-284c-499f-d9b8-4f5b2df1347d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 360
        }
      },
      "source": [
        "print(model['father'])"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[-0.08238544  0.7577278   0.27293247 -0.3334733  -0.56921965 -0.48892498\n",
            " -0.14279953 -0.15808755 -0.22058964  0.05064057 -0.45908195  0.1093078\n",
            "  0.66207737  0.15748964  0.38302854  0.92915934 -0.16326886 -0.15825947\n",
            " -0.32018897  0.26423243  1.2035353   0.31126532  0.01696637 -0.4062133\n",
            "  0.30572274  0.21858518 -0.24241619 -0.28024235  0.46816328 -1.0146354\n",
            "  0.5244162  -0.81886154  0.34656173 -0.03397862 -0.2783776  -0.1485936\n",
            "  0.10192417  0.60047096 -0.10777876  0.16814663 -0.4622436   0.1349658\n",
            " -0.86193943  0.20544118  0.24751526 -0.40783104  0.01558308  0.05697175\n",
            "  0.12315552 -0.7732856   0.3184641  -0.355033    0.08404291  0.17309989\n",
            "  0.35239208  0.07028804  0.55139965  0.23149797  0.70555925 -0.12569797\n",
            "  0.6400002   0.57075894  0.18614599 -0.16386566 -0.60103184 -0.24332406\n",
            " -0.6301399  -0.39652705  0.38290682 -0.20248339  0.18737687 -0.14003484\n",
            " -0.20123945 -0.5462016   0.53465396 -0.24130276  0.18738352  0.14594115\n",
            "  0.2839181   0.44689053  0.04513579  0.05993508 -0.803856    0.16739245\n",
            " -0.31731492 -0.01746646  0.083175   -0.13349022 -1.0094737   0.36435115\n",
            " -0.35055348  0.4092174   0.03085327  0.21108332 -0.3995651  -0.25008246\n",
            "  0.47917402  0.05309804 -0.20031953 -0.16192085]\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:1: DeprecationWarning: Call to deprecated `__getitem__` (Method will be removed in 4.0.0, use self.wv.__getitem__() instead).\n",
            "  \"\"\"Entry point for launching an IPython kernel.\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wFKMaCvoQfjg",
        "colab_type": "code",
        "outputId": "32d8987e-ff0a-458b-f0e3-7c61fb66015c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 54
        }
      },
      "source": [
        "print('sentence: ', sentences[2])"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "sentence:  ['The', 'September-October', 'term', 'jury', 'had', 'been', 'charged', 'by', 'Fulton', 'Superior', 'Court', 'Judge', 'Durwood', 'Pye', 'to', 'investigate', 'reports', 'of', 'possible', '``', 'irregularities', \"''\", 'in', 'the', 'hard-fought', 'primary', 'which', 'was', 'won', 'by', 'Mayor-nominate', 'Ivan', 'Allen', 'Jr.', '.']\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pbvCqxuxQzec",
        "colab_type": "code",
        "outputId": "823a0892-08a8-482d-88d2-c7eae7ebe1e9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "data.shape"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(57340, 7)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Y28vLcnqRS-3",
        "colab_type": "code",
        "outputId": "326abca2-8cc1-42a4-fe1d-32f8c3e7b64a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 173
        }
      },
      "source": [
        "data[['filename']].describe()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>filename</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>57340</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>unique</th>\n",
              "      <td>500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>top</th>\n",
              "      <td>ck07</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>freq</th>\n",
              "      <td>240</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "       filename\n",
              "count     57340\n",
              "unique      500\n",
              "top        ck07\n",
              "freq        240"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 26
        }
      ]
    }
  ]
}