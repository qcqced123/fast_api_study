<script>
    import fastapi from "../lib/api"
    import {link} from 'svelte-spa-router' // if you want to use link, import this line
    let question_list = []
  
    function get_question_list() {
      fastapi('get', '/api/question/list', {}, (json) => { //success_callback
        question_list = json
      }) // not init failure_callback parameter: fastapi automatically alert & print error
    }
  
    get_question_list()
    // hash based routing
  </script>
  
  <ul>
    {#each question_list as question}
      <li><a use:link href="/detail/{question.id}">{question.subject}</a></li>
    {/each}
  </ul>