<script>
    import Router from 'svelte-spa-router'
    import Home from "./routes/Home.svelte"
  
    // Define url rule
    const routes = {
      '/': Home,
      '/detail/:question_id': Detail, // 가변값을 url에 포함하는 경우
    }
  </script>
  
  <Router {routes}/>