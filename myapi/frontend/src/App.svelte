<script>
    import Router from 'svelte-spa-router'
    import Home from "./routes/Home.svelte"
    import Detail from "./routes/Detail.svelte"
    import QuestionCreate from "./routes/QuestionCreate.svelte"
    import Navigation from './components/Navigation.svelte'
    import UserCreate from "./routes/UserCreate.svelte"
    import UserLogin from "./routes/UserLogin.svelte"


    // Define url rule
    const routes = {
      '/': Home,
      '/detail/:question_id': Detail, // 가변값을 url에 포함하는 경우
      '/question-create': QuestionCreate,
      '/user-create': UserCreate,
      '/user-login': UserLogin,
    }
  </script>
  
  <Navigation />
  <Router {routes}/>