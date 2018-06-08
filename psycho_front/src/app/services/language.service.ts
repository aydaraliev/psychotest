import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import {QuestionsResponse} from '../classes/questionsResponse';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class LanguageService {
  private apiUrl = 'http://127.0.0.1:5000';  // URL to web
  object = null;
  textResults = null;

  constructor(
    private http: HttpClient,
  ) { }

  public lang = 0;

  getLanguage(): number {
    return this.lang;
  }

  changeLanguage(lang: number): void {
    this.lang = lang;
    localStorage.setItem('lang', `${lang}`);
  }

  getQuestions (id: number): Observable<QuestionsResponse> {
    const url = `${this.apiUrl}/tests/${id}`;
    return this.http.get<QuestionsResponse>(url);
  }

  saveResults (object: any) {
<<<<<<< HEAD
    return localStorage.setItem('results', JSON.stringify(object));
  };

  getResultsText (object: any): Observable<Object> {
    const url = `${this.apiUrl}/results`;
    console.log(object)
=======
    this.object = object;
  };

  getResultsText (object: any): Observable<Object> {
    const url = `${this.apiUrl}/user`;
>>>>>>> 847119bdfaf9dc2cfe35158144da5e300073d5d4

    return this.http.get<Object>(url, object);
  }

  sendUser (object: any): Observable<Object> {
<<<<<<< HEAD
    const url = `${this.apiUrl}/user`;
    const sendingObject = {
      user: object,
      results: JSON.parse(localStorage.getItem('results'))
    };
    console.log(sendingObject)
    localStorage.removeItem('results')
=======
    const url = `${this.apiUrl}/results`;
    const sendingObject = {
      user: object,
      results: this.object
    };
>>>>>>> 847119bdfaf9dc2cfe35158144da5e300073d5d4
    return this.http.post<Object>(url, sendingObject, httpOptions);
  }

  saveResultsText (object: any) {
    this.textResults = object;
  }
}
