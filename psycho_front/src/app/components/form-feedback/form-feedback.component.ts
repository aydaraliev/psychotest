import {Component, DoCheck} from '@angular/core';
import { LanguageService } from '../../services/language.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-form-feedback',
  templateUrl: './form-feedback.component.html',
  styleUrls: ['./form-feedback.component.scss'],
  providers: [LanguageService]
})

export class FormFeedbackComponent implements DoCheck {
  dob = JSON.parse(localStorage.getItem('dob')) || '';
  gender = '';
  country = 'Кыргызская Республика';
  nationality = '';
  education = '';
  family = '';
  work = '';
  city = '';
  email = '';
  sendEmail = false;

  constructor(
    private langService: LanguageService,
    private router: Router
  ) { }

  ngDoCheck() {
    // this.lang = Number(localStorage.lang);
  }

  onSubmit() {
    const sendingObject = {
      dob: this.dob,
      gender: this.gender,
      country: this.country,
      nationality: this.nationality,
      education: this.education,
      family: this.family,
      work: this.work,
      city: this.city,
      email: this.email,
      sendEmail: this.sendEmail
    };
    this.langService.sendUser(sendingObject)
      .subscribe(
        response => {
          localStorage.setItem('text-results', JSON.stringify(response.response));
          this.router.navigate(['/results']);
        },
        error => console.log(error)
      );
  }
}
