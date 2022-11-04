Vue.createApp({
  data() {
    return {
      name: "",
      surname: "",
      date: "",
      option: "",
      arrayForm: [],
      arrayNames: ['Nombre', 'Apelldio', 'Fecha', 'Sexo'],
      imgUrl: ''
    };
  },
  methods: {
    popup() {
      let arrayElementos = [];
      arrayElementos.push(this.name, this.surname, this.date, this.option);
      this.arrayForm = arrayElementos;
      this.verificacion()
    },
    verificacion() {
      if (this.arrayForm.includes('')) {
        
        setTimeout(() => {
          this.imgUrl = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPblUBOFDxlzwquIev_BEvlhTK-wW6zzTvjY3yrlCQdpLJGPmHrD0hS6yUC8DLLO3mELo&usqp=CAU'
        }, 250);

        this.imgUrl = 'https://www.gifcen.com/wp-content/uploads/2021/04/hitler-gif-1.gif'
      } else {
        this.arrayForm = []
        this.imgUrl = 'https://gifimage.net/wp-content/uploads/2017/10/muy-bien-gif-11.gif'
      }
      this.name = ''
      this.surname = ''
      this.date = ''
      this.option = ''
    }
  },
}).mount("#app");
