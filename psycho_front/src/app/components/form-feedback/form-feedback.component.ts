import {Component, DoCheck, OnInit} from '@angular/core';
import { LanguageService } from '../../services/language.service';
import { Router } from '@angular/router';
declare var $: any;

@Component({
  selector: 'app-form-feedback',
  templateUrl: './form-feedback.component.html',
  styleUrls: ['./form-feedback.component.scss'],
  providers: [LanguageService]
})

export class FormFeedbackComponent implements DoCheck, OnInit {
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

  ngOnInit() {
    $('#dob').datepicker([]);
  }

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
        },
        error => console.log(error)
      );
    this.router.navigate(['/results']);
  }
}
