package com.setonfire.animatedquizapp

object Constants {
    const val USER_NAME: String ="user_name"
    const val TOTAL_QUESTIONS: String = "total_questions"
    const val CORRECT_ANSWERS:String = "correct_answers"

    fun getQuestions(): ArrayList<Question>{
        val questionList = ArrayList<Question>()

        val que1 = Question(
            1,"Guess the animal",
            R.drawable.cow,
            "Cat", "Cow","Dog","Giraffe",
            2,
        )

        val que2 = Question(
            2,"Guess the animal",
            R.drawable.dog,
            "Cow", "Tiger","Dog","Giraffe",
            3,
        )

        val que3 = Question(
            3,"Guess the animal",
            R.drawable.cat,
            "Cat", "Lion","Dog","Tiger",
            1,
        )

        val que4 = Question(
            4,"Guess the animal",
            R.drawable.giraffe,
            "Cat", "Cow","Dog","Giraffe",
            4,
        )


        val que5 = Question(
            5,"Guess the animal",
            R.drawable.lion,
            "Dog", "Crocodile","Lion","Elephant",
            3,
        )
        val que6 = Question(
            6,"Guess the animal",
            R.drawable.tiger,
            "Tiger", "Lion","Dog","Monkey",
            1,
        )
        val que7 = Question(
            7,"Guess the animal",
            R.drawable.elephant,
            "Monkey", "Elephant","Dog","Giraffe",
            2,
        )
        val que8 = Question(
            8,"Guess the animal",
            R.drawable.monkey,
            "Cat", "Cow","Dog","monkey",
            4,
        )
        val que9 = Question(
            9,"Guess the animal",
            R.drawable.zebra,
            "Horse", "Cat","Zebra","Tiger",
            3,
        )
        val que10 = Question(
            10,"Guess the animal",
            R.drawable.crocodile,
            "Crocodile", "Dog","Lion","Elephant",
            1,
        )
        questionList.add(que1)
        questionList.add(que2)
        questionList.add(que3)
        questionList.add(que4)
        questionList.add(que5)
        questionList.add(que6)
        questionList.add(que7)
        questionList.add(que8)
        questionList.add(que9)
        questionList.add(que10)
        return questionList
    }
}