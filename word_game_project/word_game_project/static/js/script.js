$(document).ready(function() {

    $('#btnStartGame').on('click', function() {
        event.preventDefault();
        $('#btnStartGame').empty();
        var gameElementsHTML =
            `<label>
            <span class="prompt">Word:</span>
            <input id="txtNewWord" autofocus="">
      </label>
            <br><br>
            <button id="btnAddWord" class="btn btn-primary">Send</button>`
        $('#GameElements').prepend(gameElementsHTML);
        startGame();
    });

});

var words;
var coded_words;
var score;
var words_found = [];


function startGame() {

    var seconds_left = 30;
    var interval = setInterval(function() {
        document.getElementById('timer').innerHTML = `<p> Seconds left : ` + --seconds_left + `</p>`;
        if (seconds_left <= 0) {
            clearInterval(interval);
        }
    }, 1000);

    timeoutID = window.setTimeout(getScores, 30000);
    words = [];
    coded_words = [];
    score = 0;
    getNewWord()

    $('#btnAddWord').on('click', function() {
        event.preventDefault();
        var index = words.length - 1
        var index_coded = coded_words.length - 1
        var word = words[index]
        var coded_word = coded_words[index_coded]
        var word_string = word.word
        var category = word.category
        console.log()
        var flag = checkWord(word_string)
        if (flag == false) {
            // cas ou le mot n'est pas trouvé : il faut render le mot

            $('#txtNewWord').val('');
        } else {
            $('#coded_word').empty();
            $('#txtNewWord').val('');
            getNewWord();

        };

    });

    $('#txtNewWord').on('keypress', function(event) {
        if (event.which == 13) {
            event.preventDefault();
            var index = words.length - 1
            var index_coded = coded_words.length - 1
            var word = words[index]
            var coded_word = coded_words[index_coded]
            var word_string = word.word
            var category = word.category


            var flag = checkWord(word_string)
            if (flag == false) {
                // cas ou le mot n'est pas trouvé : il faut render le mot

                $('#txtNewWord').val('');
            } else {
                $('#coded_word').empty();
                $('#txtNewWord').val('');
                score += 1;
                words_found.push(word_string);
                getNewWord();
            };
        }
    });

    function getNewWord() {

        $.ajax({
                url: '/game_app/get_word/',
                type: 'GET',
            })
            .done(function(data) {
                if (data.code == 200) {
                    // récupération de l'objet word 
                    var word = data.word

                    // récupération du mot converti en code
                    var word_coded = data.coded_word

                    // récupération du mot en string 
                    var word_string = word.word

                    // récupération de la catégorie du mot
                    var category = word.category

                    // ajout de l'objet mot à la liste d'objets javascript
                    words.push(word)
                    coded_words.push(word_coded)


                    console.log(word_string)
                    render(word_coded, category)

                    // récupération de true ou false si trouvé ou non


                }
            })
    };

};

function getScores() {
    console.log(words_found)

    $.ajax({
            url: '/game_app/end_game/',
            type: 'POST',
            data: {
                words_found: JSON.stringify(words_found),
                score: score
            }
        })
        .done(function(data) {
            if (data.code == 200) {
                console.log('game created')
            }
        });


    $('#all_game').empty();

    var scoreHTML = `<div class="card-body" id="score">
                        <h4 class='text-center'> Enf of the Game </h4
                        <br> <br>
                        <h3 class='text-center'> Your Score </h3>
                        <h4>` + score + ` words </h4> <br>
                    </div>`

    $('#all_game').prepend(scoreHTML);

    $('#score').append(`<p class='text-center>`)

    for (var i = 0; i < words_found.length; i++) {
        var listHTML = words_found[i] + `, `
        $('#score').append(listHTML);
    };

    $('#score').append(`</p>`)

    var startGameHTML = `<div id="btnStartNewGame">
                    <button class="btn btn-primary">Start a New game</button>
                </div>`

    $('#score').append(startGameHTML);


    $('#btnStartNewGame').on('click', function() {
        event.preventDefault();
        $('#all_game').empty();
        var newGameHTML = `
            <div class="card-body col-sm-8">
                    <div id="btnStartGame">
                    </div>

                    <br><br>
                    <div id = 'timer'>
                    </div>
                    <div id = 'coded_word'>
                    </div>

                    <div id="GameElements">
                            <label>
                                <span class="prompt">Word:</span>
                                <input id="txtNewWord" autofocus="">
                            </label>
                            <br><br>
                            <button id="btnAddWord" class="btn btn-primary">Send</button>
                    </div>
            </div>

            <div id = 'image_keyboard'>
                 <div class='col-sm-2' >
                    <img src='/static/images/clavier.png' style='max-width: 300px;max-height: 300px'>
                </div>
            </div>`


        $('#all_game').append(newGameHTML);
        startGame();
    });


};



function render(coded_word, category) {
    console.log(coded_word)
    var wordHTML = ` 
        <h4> ` + category + ` </h4>
        <h5 class="card-title">` + coded_word + `</h5>`;
    $('#coded_word').prepend(wordHTML);

};

function checkWord(word_to_find) {
    var word = $('#txtNewWord').val()
    check = false
    if (word_to_find == word) {
        check = true
    }
    return check
};



$(document).ready(function () {
$(function() {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
        var host = document.location.host;
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}); 

});
