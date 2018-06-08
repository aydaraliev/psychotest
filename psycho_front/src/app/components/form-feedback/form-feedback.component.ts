import { Component, DoCheck } from '@angular/core';
// import { LanguageService } from '../../services/language.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-form-feedback',
  templateUrl: './form-feedback.component.html',
  styleUrls: ['./form-feedback.component.scss']
})

export class FormFeedbackComponent implements DoCheck {
  lang = 0;
  title = ['Помогите нам улучшить наши исследования', 'Келгиле, биздин изилдөө жакшыртууга жардам берет'];
  /* tslint:disable */
  subtitle = ['Все ответы являются необязательными. Если вы предпочитаете не отвечать на какой-либо конкретный вопрос, это прекрасно, если оставить его пустым. Любые данные, которые вы согласны предоставить, будут полезны.', 'Бардык жооптор бар. Сиз, балким, бир суроого жооп эмес, керек болсо, ал аны бош калтырып үчүн жакшы. Сиз камсыз кылууга макул болбосун маалыматтар жардам берет.'];
  /* tslint:enable */
  dob = ['Дата рождения', 'Туулган датасы'];
  country = ['Я родился в', 'Мен төрөлгөм'];
  gender = ['Пол', 'Калаасы'];

  constructor(
    // private langService: LanguageService,
    private router: Router
  ) { }

  ngDoCheck() {
    this.lang = Number(localStorage.lang);
  }

  onSubmit() {
    this.router.navigate(['/results']);
  }
}
