import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import { QuestionsResponse } from '../classes/questionsResponse';
import { Response} from "../classes/response";
import { Voter } from "../classes/voter";
import { VoterObject } from "../classes/voterObject";

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class LanguageService {
  private apiUrl = 'http://127.0.0.1:5000' //'http://188.166.88.156'; //'http://188.166.88.156';  // URL to web
  object = null;

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
    return localStorage.setItem('results', JSON.stringify(object));
  };

  sendUser (object: any): Observable<Response> {
    const url = `${this.apiUrl}/tests/results`;
    const sendingObject = {
      user: object,
      results: JSON.parse(localStorage.getItem('results')),
      voter: JSON.parse(localStorage.getItem('voter')),
      responses: JSON.parse(localStorage.getItem('backQuestions')),
    };
    // localStorage.removeItem('results');
    localStorage.removeItem('voter');
    return this.http.post<Response>(url, sendingObject, httpOptions);
  };

  findVoted (lastname: string, firstname: string, birthday: string): Observable<Voter> {
    const url = `${this.apiUrl}/tests/voter`;
    const uuid4 = JSON.parse(localStorage.getItem('uuid4'));

    const sendingObject = { firstname, lastname, birthday, uuid4 };

    return this.http.post<Voter>(url, sendingObject, httpOptions)
  };

  getResults () {
    return JSON.parse(localStorage.getItem('text-results'));
  }

  foundNotFound (voter): Observable<VoterObject> {
    const url = `${this.apiUrl}/tests/found_not_found`;
    const uuid4 = JSON.parse(localStorage.getItem('uuid4'));
    const found_presidential = voter.presidential;
    const found_parliamentary = voter.parliamentary;

    const sendingObject = { found_presidential, found_parliamentary, uuid4 };

    return this.http.post<VoterObject>(url, sendingObject, httpOptions);
  }
}
