var app = new Vue({
    el: '#root',
    data: {
      activeStep: 0,
      steps: [
        {text: 'Choose a Model'},
        {text: 'Make a query'},
        {text: 'Evaluate'},
      ]
    },
    methods: {
      load_vector_model: function() {
        // Vector Model call here
        console.log("aaaa");
        this.activeStep++;
      },
      load_latent_model() {
        // Latent Semantic model here
        this.activeStep++;
      }
    }
  })