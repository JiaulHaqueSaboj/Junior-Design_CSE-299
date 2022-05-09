package com.example.androidproject.Api.Prediction;

import com.example.androidproject.model.PredictionModel;
import com.example.androidproject.model.SearchModel;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Query;

public interface predictionApi {

    @GET("predict")
    Call<List<PredictionModel>> getPrediction (@Query("age_first_funding_year") float age_first_funding_year,
                                               @Query("age_last_funding_year") float age_last_funding_year,
                                               @Query("age_first_milestone_year") float age_first_milestone_year,
                                               @Query("age_last_milestone_year") float age_last_milestone_year,
                                               @Query("relationships") float relationships,
                                               @Query("funding_rounds") float funding_rounds,
                                               @Query("funding_total_usd") float funding_total_usd,
                                               @Query("milestones") float milestones,
                                               @Query("is_software") int is_software,
                                               @Query("is_web") int is_web,
                                               @Query("is_mobile") int is_mobile,
                                               @Query("is_enterprise") int is_enterprise,
                                               @Query("is_advertising") int is_advertising,
                                               @Query("is_gamesvideo") int is_gamesvideo,
                                               @Query("is_ecommerce") int is_ecommerce,
                                               @Query("is_biotech") int is_biotech,
                                               @Query("is_consulting") int is_consulting,
                                               @Query("is_othercategory") int is_othercategory,
                                               @Query("avg_participants") float avg_participants,
                                               @Query("has_RoundABCD") float has_RoundABCD,
                                               @Query("has_Investor") float has_Investor,
                                               @Query("has_Seed") float has_Seed,
                                               @Query("invalid_startup") float invalid_startup,
                                               @Query("startUp_age_year") float startUp_age_year);//@Header("Authorization") String token
}
