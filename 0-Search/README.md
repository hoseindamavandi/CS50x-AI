# CS50x-AI
### Search

<details>
    <summary>degrees</summary>
    <br>
    <main class="col-md" style="margin-bottom: 564px; margin-top: 82px;">

<a data-id="" id="degrees" style="top: -82px;"></a><h1><a data-id="" href="#degrees">Degrees</a></h1>

<p>Write a program that determines how many “degrees of separation” apart two actors are.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ python degrees.py large
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
</code></pre></div></div>

<a data-id="" id="background" style="top: -82px;"></a><h2><a data-id="" href="#background">Background</a></h2>

<p>According to the <a href="https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon">Six Degrees of Kevin Bacon</a> game, anyone in the Hollywood film industry can be connected to Kevin Bacon within six steps, where each step consists of finding a film that two actors both starred in.</p>

<p>In this problem, we’re interested in finding the shortest path between any two actors by choosing a sequence of movies that connects them. For example, the shortest path between Jennifer Lawrence and Tom Hanks is 2: Jennifer Lawrence is connected to Kevin Bacon by both starring in “X-Men: First Class,” and Kevin Bacon is connected to Tom Hanks by both starring in “Apollo 13.”</p>

<p>We can frame this as a search problem: our states are people. Our actions are movies, which take us from one actor to another (it’s true that a movie could take us to multiple different actors, but that’s okay for this problem). Our initial state and goal state are defined by the two people we’re trying to connect. By using breadth-first search, we can find the shortest path from one actor to another.</p>
Specification
<a data-id="" id="understanding" style="top: -82px;"></a><h2><a data-id="" href="#understanding">Understanding</a></h2>

<p>The distribution code contains two sets of CSV data files: one set in the <code class="language-plaintext highlighter-rouge">large</code> directory and one set in the <code class="language-plaintext highlighter-rouge">small</code> directory. Each contains files with the same names, and the same structure, but <code class="language-plaintext highlighter-rouge">small</code> is a much smaller dataset for ease of testing and experimentation.</p>

<p>Each dataset consists of three CSV files. A CSV file, if unfamiliar, is just a way of organizing data in a text-based format: each row corresponds to one data entry, with commas in the row separating the values for that entry.</p>

<p>Open up <code class="language-plaintext highlighter-rouge">small/people.csv</code>. You’ll see that each person has a unique <code class="language-plaintext highlighter-rouge">id</code>, corresponding with their <code class="language-plaintext highlighter-rouge">id</code> in <a href="https://www.imdb.com/">IMDb</a>’s database. They also have a <code class="language-plaintext highlighter-rouge">name</code>, and a <code class="language-plaintext highlighter-rouge">birth</code> year.</p>

<p>Next, open up <code class="language-plaintext highlighter-rouge">small/movies.csv</code>. You’ll see here that each movie also has a unique <code class="language-plaintext highlighter-rouge">id</code>, in addition to a <code class="language-plaintext highlighter-rouge">title</code> and the <code class="language-plaintext highlighter-rouge">year</code> in which the movie was released.</p>

<p>Now, open up <code class="language-plaintext highlighter-rouge">small/stars.csv</code>. This file establishes a relationship between the people in <code class="language-plaintext highlighter-rouge">people.csv</code> and the movies in <code class="language-plaintext highlighter-rouge">movies.csv</code>. Each row is a pair of a <code class="language-plaintext highlighter-rouge">person_id</code> value and <code class="language-plaintext highlighter-rouge">movie_id</code> value. The first row (ignoring the header), for example, states that the person with id 102 starred in the movie with id 104257. Checking that against <code class="language-plaintext highlighter-rouge">people.csv</code> and <code class="language-plaintext highlighter-rouge">movies.csv</code>, you’ll find that this line is saying that Kevin Bacon starred in the movie “A Few Good Men.”</p>

<p>Next, take a look at <code class="language-plaintext highlighter-rouge">degrees.py</code>. At the top, several data structures are defined to store information from the CSV files. The <code class="language-plaintext highlighter-rouge">names</code> dictionary is a way to look up a person by their name: it maps names to a set of corresponding ids (because it’s possible that multiple actors have the same name). The <code class="language-plaintext highlighter-rouge">people</code> dictionary maps each person’s id to another dictionary with values for the person’s <code class="language-plaintext highlighter-rouge">name</code>, <code class="language-plaintext highlighter-rouge">birth</code> year, and the set of all the <code class="language-plaintext highlighter-rouge">movies</code> they have starred in. And the <code class="language-plaintext highlighter-rouge">movies</code> dictionary maps each movie’s id to another dictionary with values for that movie’s <code class="language-plaintext highlighter-rouge">title</code>, release <code class="language-plaintext highlighter-rouge">year</code>, and the set of all the movie’s <code class="language-plaintext highlighter-rouge">stars</code>. The <code class="language-plaintext highlighter-rouge">load_data</code> function loads data from the CSV files into these data structures.</p>

<p>The <code class="language-plaintext highlighter-rouge">main</code> function in this program first loads data into memory (the directory from which the data is loaded can be specified by a command-line argument). Then, the function prompts the user to type in two names. The <code class="language-plaintext highlighter-rouge">person_id_for_name</code> function retrieves the id for any person (and handles prompting the user to clarify, in the event that multiple people have the same name). The function then calls the <code class="language-plaintext highlighter-rouge">shortest_path</code> function to compute the shortest path between the two people, and prints out the path.</p>

<p>The <code class="language-plaintext highlighter-rouge">shortest_path</code> function, however, is left unimplemented. That’s where you come in!</p>

<a data-id="" id="specification" style="top: -82px;"></a><h2><a data-id="" href="#specification">Specification</a></h2>

<div class="alert alert-warning" data-alert="warning" role="alert"><p>An automated tool assists the staff in enforcing the constraints in the below specification. Your submission will fail if any of these are not handled properly, if you import modules other than those explicitly allowed, or if you modify functions other than as permitted.</p></div>

<p>Complete the implementation of the <code class="language-plaintext highlighter-rouge">shortest_path</code> function such that it returns the shortest path from the person with id <code class="language-plaintext highlighter-rouge">source</code> to the person with the id <code class="language-plaintext highlighter-rouge">target</code>.</p>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Assuming there is a path from the <code class="language-plaintext highlighter-rouge">source</code> to the <code class="language-plaintext highlighter-rouge">target</code>, your function should return a list, where each list item is the next <code class="language-plaintext highlighter-rouge">(movie_id, person_id)</code> pair in the path from the source to the target. Each pair should be a tuple of two strings.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>For example, if the return value of <code class="language-plaintext highlighter-rouge">shortest_path</code> were <code class="language-plaintext highlighter-rouge">[(1, 2), (3, 4)]</code>, that would mean that the source starred in movie 1 with person 2, person 2 starred in movie 3 with person 4, and person 4 is the target.</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If there are multiple paths of minimum length from the source to the target, your function can return any of them.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If there is no possible path between two actors, your function should return <code class="language-plaintext highlighter-rouge">None</code>.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>You may call the <code class="language-plaintext highlighter-rouge">neighbors_for_person</code> function, which accepts a person’s id as input, and returns a set of <code class="language-plaintext highlighter-rouge">(movie_id, person_id)</code> pairs for all people who starred in a movie with a given person.</li>
</ul>

<p>You should not modify anything else in the file other than the <code class="language-plaintext highlighter-rouge">shortest_path</code> function, though you may write additional functions and/or import other Python standard library modules.</p>


</main>

  </details>


<details>
    <summary>Tic Tac Toe</summary>
    <br>

<main class="col-md" style="margin-bottom: 0px; margin-top: 82px;">
<a data-id="" id="tic-tac-toe" style="top: -82px;"></a><h1><a data-id="" href="#tic-tac-toe">Tic-Tac-Toe</a></h1>

<p>Using Minimax, implement an AI to play Tic-Tac-Toe optimally.</p>

![image](https://user-images.githubusercontent.com/83751182/152701845-3aeb1691-7d92-464c-9780-aa0c68770387.png)


<a data-id="" id="understanding" style="top: -82px;"></a><h2><a data-id="" href="#understanding">Understanding</a></h2>

<p>There are two main files in this project: <code class="language-plaintext highlighter-rouge">runner.py</code> and <code class="language-plaintext highlighter-rouge">tictactoe.py</code>. <code class="language-plaintext highlighter-rouge">tictactoe.py</code> contains all of the logic for playing the game, and for making optimal moves. <code class="language-plaintext highlighter-rouge">runner.py</code> has been implemented for you, and contains all of the code to run the graphical interface for the game. Once you’ve completed all the required functions in <code class="language-plaintext highlighter-rouge">tictactoe.py</code>, you should be able to run <code class="language-plaintext highlighter-rouge">python runner.py</code> to play against your AI!</p>

<p>Let’s open up <code class="language-plaintext highlighter-rouge">tictactoe.py</code> to get an understanding for what’s provided. First, we define three variables: <code class="language-plaintext highlighter-rouge">X</code>, <code class="language-plaintext highlighter-rouge">O</code>, and <code class="language-plaintext highlighter-rouge">EMPTY</code>, to represent possible moves of the board.</p>

<p>The function <code class="language-plaintext highlighter-rouge">initial_state</code> returns the starting state of the board. For this problem, we’ve chosen to represent the board as a list of three lists (representing the three rows of the board), where each internal list contains three values that are either <code class="language-plaintext highlighter-rouge">X</code>, <code class="language-plaintext highlighter-rouge">O</code>, or <code class="language-plaintext highlighter-rouge">EMPTY</code>.
What follows are functions that we’ve left up to you to implement!</p>

<a data-id="" id="specification" style="top: -82px;"></a><h2><a data-id="" href="#specification">Specification</a></h2>

<div class="alert alert-warning" data-alert="warning" role="alert"><p>An automated tool assists the staff in enforcing the constraints in the below specification. Your submission will fail if any of these are not handled properly, if you import modules other than those explicitly allowed, or if you modify functions other than as permitted.</p></div>

<p>Complete the implementations of <code class="language-plaintext highlighter-rouge">player</code>, <code class="language-plaintext highlighter-rouge">actions</code>, <code class="language-plaintext highlighter-rouge">result</code>, <code class="language-plaintext highlighter-rouge">winner</code>, <code class="language-plaintext highlighter-rouge">terminal</code>, <code class="language-plaintext highlighter-rouge">utility</code>, and <code class="language-plaintext highlighter-rouge">minimax</code>.</p>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The <code class="language-plaintext highlighter-rouge">player</code> function should take a <code class="language-plaintext highlighter-rouge">board</code> state as input, and return which player’s turn it is (either <code class="language-plaintext highlighter-rouge">X</code> or <code class="language-plaintext highlighter-rouge">O</code>).
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>In the initial game state, <code class="language-plaintext highlighter-rouge">X</code> gets the first move. Subsequently, the player alternates with each additional move.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The <code class="language-plaintext highlighter-rouge">actions</code> function should return a <code class="language-plaintext highlighter-rouge">set</code> of all of the possible actions that can be taken on a given board.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Each action should be represented as a tuple <code class="language-plaintext highlighter-rouge">(i, j)</code> where <code class="language-plaintext highlighter-rouge">i</code> corresponds to the row of the move (<code class="language-plaintext highlighter-rouge">0</code>, <code class="language-plaintext highlighter-rouge">1</code>, or <code class="language-plaintext highlighter-rouge">2</code>) and <code class="language-plaintext highlighter-rouge">j</code> corresponds to which cell in the row corresponds to the move (also <code class="language-plaintext highlighter-rouge">0</code>, <code class="language-plaintext highlighter-rouge">1</code>, or <code class="language-plaintext highlighter-rouge">2</code>).</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Possible moves are any cells on the board that do not already have an <code class="language-plaintext highlighter-rouge">X</code> or an <code class="language-plaintext highlighter-rouge">O</code> in them.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Any return value is acceptable if a terminal board is provided as input.</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The <code class="language-plaintext highlighter-rouge">result</code> function takes a <code class="language-plaintext highlighter-rouge">board</code> and an <code class="language-plaintext highlighter-rouge">action</code> as input, and should return a new board state, without modifying the original board.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If <code class="language-plaintext highlighter-rouge">action</code> is not a valid action for the board, your program should <a href="https://docs.python.org/3/tutorial/errors.html#raising-exceptions">raise an exception</a>.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The returned board state should be the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell in <code class="language-plaintext highlighter-rouge">board</code> itself is not a correct implementation of the <code class="language-plaintext highlighter-rouge">result</code> function. You’ll likely want to make a <a href="https://docs.python.org/3/library/copy.html#copy.deepcopy">deep copy</a> of the board first before making any changes.</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The <code class="language-plaintext highlighter-rouge">winner</code> function should accept a <code class="language-plaintext highlighter-rouge">board</code> as input, and return the winner of the board if there is one.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If the X player has won the game, your function should return <code class="language-plaintext highlighter-rouge">X</code>. If the O player has won the game, your function should return <code class="language-plaintext highlighter-rouge">O</code>.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>One can win the game with three of their moves in a row horizontally, vertically, or diagonally.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return <code class="language-plaintext highlighter-rouge">None</code>.</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The <code class="language-plaintext highlighter-rouge">terminal</code> function should accept a <code class="language-plaintext highlighter-rouge">board</code> as input, and return a boolean value indicating whether the game is over.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return <code class="language-plaintext highlighter-rouge">True</code>.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>Otherwise, the function should return <code class="language-plaintext highlighter-rouge">False</code> if the game is still in progress.</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The <code class="language-plaintext highlighter-rouge">utility</code> function should accept a terminal <code class="language-plaintext highlighter-rouge">board</code> as input and output the utility of the board.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If X has won the game, the utility is <code class="language-plaintext highlighter-rouge">1</code>. If O has won the game, the utility is <code class="language-plaintext highlighter-rouge">-1</code>. If the game has ended in a tie, the utility is <code class="language-plaintext highlighter-rouge">0</code>.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>You may assume <code class="language-plaintext highlighter-rouge">utility</code> will only be called on a <code class="language-plaintext highlighter-rouge">board</code> if <code class="language-plaintext highlighter-rouge">terminal(board)</code> is <code class="language-plaintext highlighter-rouge">True</code>.</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The <code class="language-plaintext highlighter-rouge">minimax</code> function should take a <code class="language-plaintext highlighter-rouge">board</code> as input, and return the optimal move for the player to move on that board.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>The move returned should be the optimal action <code class="language-plaintext highlighter-rouge">(i, j)</code> that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-square"></i></span>If the <code class="language-plaintext highlighter-rouge">board</code> is a terminal board, the <code class="language-plaintext highlighter-rouge">minimax</code> function should return <code class="language-plaintext highlighter-rouge">None</code>.</li>
    </ul>
  </li>
</ul>

<p>For all functions that accept a <code class="language-plaintext highlighter-rouge">board</code> as input, you may assume that it is a valid board (namely, that it is a list that contains three rows, each with three values of either <code class="language-plaintext highlighter-rouge">X</code>, <code class="language-plaintext highlighter-rouge">O</code>, or <code class="language-plaintext highlighter-rouge">EMPTY</code>). You should not modify the function declarations (the order or number of arguments to each function) provided.</p>

<p>Once all functions are implemented correctly, you should be able to run <code class="language-plaintext highlighter-rouge">python runner.py</code> and play against your AI. And, since Tic-Tac-Toe is a tie given optimal play by both sides, you should never be able to beat the AI (though if you don’t play optimally as well, it may beat you!)</p>

</main>
    </details>
