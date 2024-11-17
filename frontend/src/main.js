import { createApp } from 'vue'
import App from './App.vue'
import Vuelidate from 'vuelidate'
import components from '@/components/UI'
import router from '@/router/router'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { faGlobe } from '@fortawesome/free-solid-svg-icons'
import { faTv } from '@fortawesome/free-solid-svg-icons'
import { faVideo } from '@fortawesome/free-solid-svg-icons'
import { faLock } from '@fortawesome/free-solid-svg-icons'
import { faShieldHalved } from '@fortawesome/free-solid-svg-icons'
import { faCircle } from '@fortawesome/free-solid-svg-icons'
import { faEye } from '@fortawesome/free-solid-svg-icons'
import { faEyeSlash } from '@fortawesome/free-solid-svg-icons'
import { faUser } from '@fortawesome/free-solid-svg-icons'
import { faEnvelope } from '@fortawesome/free-regular-svg-icons'
import { faComments } from '@fortawesome/free-regular-svg-icons'
import { faDisplay } from '@fortawesome/free-solid-svg-icons'
import { faPhone } from '@fortawesome/free-solid-svg-icons'
import { faPhoneSlash } from '@fortawesome/free-solid-svg-icons'
import { faMicrophone } from '@fortawesome/free-solid-svg-icons'
import { faMicrophoneSlash } from '@fortawesome/free-solid-svg-icons'

library.add(
  faGlobe,
  faTv,
  faVideo,
  faLock,
  faShieldHalved,
  faCircle,
  faEye,
  faEyeSlash,
  faUser,
  faEnvelope,
  faComments,
  faDisplay,
  faPhone,
  faPhoneSlash,
  faMicrophone,
  faMicrophoneSlash,
)

const app = createApp(App)

components.forEach((component) => {
  app.component(component.name, component)
})

app.use(Vuelidate).component('font-awesome-icon', FontAwesomeIcon).use(router).mount('#app')
