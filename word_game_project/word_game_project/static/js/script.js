$(document).ready(function() {

    $('#btnAddWord').on('click', function() {
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
                getNewWord();
            };
        }
    });

});

let words = []
let coded_words = []


$('#btnStartGame').on('click', function() {
    event.preventDefault();
    $('#btnStartGame').empty();
    getNewWord();
});





function render(coded_word, category) {
    console.log(coded_word)
    var wordHTML = ` 
		<h4> ` + category + ` </h4>
		<h5 class="card-title">` + coded_word + `</h5>`;
    $('#coded_word').prepend(wordHTML);

};


function getNewWord() {

    $.ajax({
            url: '/game_app/get_word/',
            type: 'GET',
            // data: {
            //     'words': words
            // }

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
}

function checkWord(word_to_find) {
    var word = $('#txtNewWord').val()
    check = false
    if (word_to_find == word) {
        check = true
    }
    return check
}