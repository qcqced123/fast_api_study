<script>
    import Router from 'svelte-spa-router'
    import Home from "./routes/Home.svelte"
    import Detail from "./routes/Detail.svelte"
    import QuestionCreate from "./routes/QuestionCreate.svelte"
    import Navigation from './components/Navigation.svelte'

    // Define url rule
    const routes = {
      '/': Home,
      '/detail/:question_id': Detail, // 가변값을 url에 포함하는 경우
      '/question-create': QuestionCreate,
    }
  </script>
  
  <Navigation />
  <Router {routes}/>