# LING 412: Computational Linguistics Assignment
# Kiswahili Noun Lexicon (20 stems across 5 noun-class pairs)

kiswahili_lexicon = [
    # Class 1/2 (Human nouns: m-/wa-)
    {"stem": "tu", "class-pair": "1/2", "sg-prefix": "m-", "pl-prefix": "wa-", "sg-form": "mtu", "pl-form": "watu", "gloss": "person"},
    {"stem": "toto", "class-pair": "1/2", "sg-prefix": "m-", "pl-prefix": "wa-", "sg-form": "mtoto", "pl-form": "watoto", "gloss": "child"},
    {"stem": "funzi", "class-pair": "1/2", "sg-prefix": "m-", "pl-prefix": "wa-", "sg-form": "mfunzi", "pl-form": "wafunzi", "gloss": "teacher/instructor"},
    {"stem": "geni", "class-pair": "1/2", "sg-prefix": "m-", "pl-prefix": "wa-", "sg-form": "mgeni", "pl-form": "wageni", "gloss": "guest/visitor"},

    # Class 3/4 (Trees & Plants / Miscellaneous: m-/mi-)
    {"stem": "ti", "class-pair": "3/4", "sg-prefix": "m-", "pl-prefix": "mi-", "sg-form": "mti", "pl-form": "miti", "gloss": "tree"},
    {"stem": "kono", "class-pair": "3/4", "sg-prefix": "m-", "pl-prefix": "mi-", "sg-form": "mkono", "pl-form": "mikono", "gloss": "hand/arm"},
    {"stem": "to", "class-pair": "3/4", "sg-prefix": "m-", "pl-prefix": "mi-", "sg-form": "mto", "pl-form": "mito", "gloss": "river"},
    {"stem": "pango", "class-pair": "3/4", "sg-prefix": "m-", "pl-prefix": "mi-", "sg-form": "mpango", "pl-form": "mipango", "gloss": "plan"},

    # Class 5/6 (Fruits, Augmentatives, etc.: ji-/ma-)
    {"stem": "ji", "class-pair": "5/6", "sg-prefix": "ji-", "pl-prefix": "ma-", "sg-form": "jiji", "pl-form": "majiji", "gloss": "city"},
    {"stem": "we", "class-pair": "5/6", "sg-prefix": "ji-", "pl-prefix": "ma-", "sg-form": "jiwe", "pl-form": "mawe", "gloss": "stone"},
    {"stem": "tunda", "class-pair": "5/6", "sg-prefix": "Ø", "pl-prefix": "ma-", "sg-form": "tunda", "pl-form": "matunda", "gloss": "fruit"},
    {"stem": "neno", "class-pair": "5/6", "sg-prefix": "Ø", "pl-prefix": "ma-", "sg-form": "neno", "pl-form": "maneno", "gloss": "word"},

    # Class 7/8 (Inanimates, Tools: ki-/vi-)
    {"stem": "tabu", "class-pair": "7/8", "sg-prefix": "ki-", "pl-prefix": "vi-", "sg-form": "kitabu", "pl-form": "vitabu", "gloss": "book"},
    {"stem": "su", "class-pair": "7/8", "sg-prefix": "ki-", "pl-prefix": "vi-", "sg-form": "kisu", "pl-form": "visu", "gloss": "knife"},
    {"stem": "atu", "class-pair": "7/8", "sg-prefix": "ki-", "pl-prefix": "vi-", "sg-form": "kiatu", "pl-form": "viatu", "gloss": "shoe"},
    {"stem": "jiko", "class-pair": "7/8", "sg-prefix": "ki-", "pl-prefix": "vi-", "sg-form": "kijiko", "pl-form": "vijiko", "gloss": "spoon"},

    # Class 9/10 (Animals, Common nouns: n-/n-)
    {"stem": "alamu", "class-pair": "9/10", "sg-prefix": "n-", "pl-prefix": "n-", "sg-form": "kalamu", "pl-form": "kalamu", "gloss": "pen"},
    {"stem": "goma", "class-pair": "9/10", "sg-prefix": "n-", "pl-prefix": "n-", "sg-form": "ngoma", "pl-form": "ngoma", "gloss": "drum"},
    {"stem": "jia", "class-pair": "9/10", "sg-prefix": "n-", "pl-prefix": "n-", "sg-form": "njia", "pl-form": "njia", "gloss": "path/way"},
    {"stem": "bwa", "class-pair": "9/10", "sg-prefix": "n-", "pl-prefix": "n-", "sg-form": "mbwa", "pl-form": "mbwa", "gloss": "dog"}
]

if __name__ == "__main__":
    print(f"Total stems collected: {len(kiswahili_lexicon)}")
    for item in kiswahili_lexicon:
        print(item)
