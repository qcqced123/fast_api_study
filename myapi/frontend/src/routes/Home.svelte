<script>
    import fastapi from "../lib/api"
    let question_list = []
  
    function get_question_list() {
      fastapi('get', '/api/question/list', {}, (json) => { //success_callback
        question_list = json
      }) // not init failure_callback parameter: fastapi automatically alert & print error
    }
  
    get_question_list()
  </script>
  
  <ul>
    {#each question_list as question}
      <li>{question.subject}</li>
    {/each}
  </ul>