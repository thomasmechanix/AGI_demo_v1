import streamlit as st
#from st_aggrid import AgGrid
import pandas as pd
import plotly.graph_objects as go

########### langchain related imports ##############
# from langchain.agents import ConversationalChatAgent, AgentExecutor
# from langchain.callbacks import StreamlitCallbackHandler
# from langchain.chat_models import ChatOpenAI
# from langchain.memory import ConversationBufferMemory
# from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
# from langchain.tools import DuckDuckGoSearchRun
####################################################
def load_demo_article():
    stuff_to_show = """Employment Data Signals Bullish Trend for U.S. Equities\n

    In a recent analysis by our quantitative models, the short-term outlook for the U.S. equities market has taken a bullish turn. The predictive strength of employment metrics, specifically the percentage change in payroll jobs month-on-month, has been validated by a SHAP value of 0.0387, marking a consistent feature of importance as indicated by its unwavering rank.
    The positive shift in employment figures is a leading indicator of economic expansion. Historically, an increase in payroll numbers correlates with elevated consumer spending levels, translating into higher corporate profitability and stock performance. These conditions often lead to a favorable environment for equity investors, particularly in sectors sensitive to consumer demand.
    A closer examination reveals that the percentage increase in payroll jobs does not occur in isolation. It is complemented by corresponding advancements in consumer sentiment, which typically presages heightened market activity. This interplay between employment and consumer confidence is crucial, as it is demonstrative of a cycle of economic reinforcement that could propel equities further.
    Sector-wise, the burgeoning employment data suggests potential growth in industries directly impacted by consumer spending habits. Technology, consumer discretionary, and financial sectors are poised to benefit from this uptick in employment. Such sectors have historically leveraged economic expansions to their advantage, often translating into outsized returns for savvy investors.
    However, a nuanced approach is warranted. The rapidity of employment growth may signal an overheating economy, leading to inflationary concerns. The delicate balance between capitalizing on immediate growth and hedging against potential inflation-induced volatility is a challenge that investors must navigate.\n
    Further, our data-driven approach incorporates the latest in consumer spending forecasts and corporate earnings reports, enriching the model's predictive capabilities. The strategic recommendations provided herein are informed by a comprehensive review of market conditions, economic indicators, and sectoral trends, all underscored by a thorough quantitative analysis.
    Given the current economic backdrop and market sentiment, our outlook remains optimistic. Yet, we maintain a vigilant stance, recognizing that market dynamics are subject to rapid change. The quantitative analysis presented is one of many tools in our arsenal, allowing us to remain adaptive and responsive to new data and shifting trends.
    The insights garnered from this rigorous analytical process are intended to guide investment decisions. They underscore the importance of continuous assessment and strategic flexibility in an ever-evolving market landscape.

    Equity Market Outlook: Interpreting Treasury Interest Rate Spreads\n
    Our machine learning model's analysis indicates a bullish short-term outlook for the U.S. equities market, a stance substantiated by recent movements in Treasury interest rate spreads over the last six months. Despite a minor contraction in SHAP values from 0.0136 to 0.0121, the spreads retain their second-place ranking in terms of economic impact on the model's forecast.
    Investor preference for longer-term maturities, as inferred from these spreads, suggests a growing confidence in the economic landscape and a readiness to assume more risk—a favorable omen for equity markets. This aligns with the historical pattern where such a preference often presages a period of robust economic activity and stock market gains.
    From a buy-side perspective, the stability of interest rate spreads indicates a supportive environment for equities. An accommodating investment landscape typically augurs well for corporate expansion and stock performance, particularly in sectors sensitive to interest rates and economic growth.\n
    Our enhanced analysis includes a time-series examination of Treasury spreads correlated with equity index performance, shedding light on the predictive influence of this indicator. Additionally, forward-looking economic metrics have been incorporated, such as GDP growth forecasts and corporate bond spreads, offering a comprehensive economic viewpoint.
    Special attention is paid to sectoral implications. Financials, for instance, tend to benefit from widening spreads, whereas consumer staples may see better performance during periods of spread contraction. This sector-specific approach informs our portfolio allocation recommendations, advocating for an overweight position in sectors exhibiting growth potential in the current yield curve environment.
    Our predictive framework takes into account the lagging nature of economic indicators, emphasizing the need for investment strategies that can adapt to rapid shifts in the economic landscape. Given the historical lag between Treasury spread movements and equity market reactions, our approach remains nimble, ready to pivot in anticipation of economic shifts.
    The research culmination suggests a strategic bias towards U.S. equities, underscoring the importance of portfolio diversification and dynamic asset allocation. Investors are encouraged to take advantage of the current economic signals while remaining prepared for potential market volatility.

    Robust Personal Consumption Expenditure Fuels Optimism in U.S. Equities\n
    In recent analysis, our machine learning model has identified a bullish signal in the short-term market outlook, driven by a notable increase in Personal Consumption Expenditure (PCE) over the last month. The surge in PCE’s SHAP value from 0.0035 to 0.0094, a rise in its rank from 17th to 3rd, underscores the economic indicator’s heightened significance.
    PCE, a primary driver of economic activity, reflects burgeoning consumer confidence and spending. The positive shift in PCE is particularly impactful for sectors such as retail and consumer discretionary, which are directly fueled by consumer spending patterns. As consumer spending goes, so often does the broader economy, making this indicator a critical focus for equity investors.
    The correlation between PCE and sector performance has been visually mapped, revealing a relationship between consumer expenditure and the stock performance of related sectors. A discernible pattern emerges, linking increases in PCE to a subsequent rise in equity prices, particularly within sectors that cater to consumer needs.\n
    This rise in consumption is a harbinger of profitability for consumer-facing companies, indicating potential for revenue growth and stock appreciation. A deeper dive into PCE components points to specific consumer behaviors, with an increase in durable goods spending indicating long-term consumer confidence, while upticks in non-durable goods highlight immediate consumption trends.
    The analysis is enriched by correlating PCE with earnings reports from major retailers and consumer goods manufacturers, providing a predictive look at the sector's health. This is complemented by additional economic data, such as wage growth and credit expansion, to assess the PCE growth trend's sustainability.
    While the current PCE trajectory supports a bullish view, it is crucial to consider the balance between credit-induced spending and wage-driven growth. The analysis has been extended to include these variables, ensuring a robust and sustainable bullish outlook. \n
    Investors are advised to consider sectors that directly benefit from consumer spending increases. The research identifies potential beneficiaries of the current trend, with a focus on companies exhibiting strong fundamentals, healthy balance sheets, and strategic market positioning.
    The updated model, now incorporating a broader array of macroeconomic indicators, reaffirms the initial bullish outlook provided by PCE data. Clients are encouraged to closely monitor these trends, which will inform portfolio management decisions, with a particular focus on sectors poised to capitalize on consumer spending.
    The sectors primed for gains, based on the current economic indicators, are highlighted, though the report emphasizes the need for risk management practices to navigate market volatility effectively. The bullish stance is advocated with the provision that strategies remain adaptable to evolving market conditions.

    Assessing the Impact of Labor Force Dynamics on U.S. Equities\n
    Recent data analyzed by our machine learning model indicates a bullish stance on the short-term horizon for U.S. equities, bolstered by the labor force's year-over-year percentage growth. The slight shift in the SHAP value from 0.0086 to 0.0093, while experiencing a nominal rank decrease, suggests an underlying strength in economic participation, which is a positive sign for the markets.
    The expansion of the civilian labor force is intrinsically linked to the vitality of the economy, influencing consumer spending and corporate profitability. An increasing labor force is indicative of a growing economy where higher employment levels support consumer demand, a cornerstone for robust equity markets.
    Our examination extends beyond raw data, plotting labor force changes against market indices to understand the historical correlation better and potential implications for future market performance. The labor force's growth, particularly when aligned with productivity gains, presents a scenario where a bullish equity market can thrive without the looming threat of inflationary pressures that might compel a shift in monetary policy.
    Investment strategies, particularly within consumer discretionary and technology sectors, may need to be recalibrated to reflect the increased spending power of a larger workforce. Stock selection within these sectors should consider companies poised to benefit from heightened consumer expenditure and those offering productivity-enhancing technologies.
    Further enriching our analysis, we've integrated productivity figures and wage growth into our model to ensure the labor force increase aligns with actual economic output and consumer spending. The quality of labor force growth, particularly the balance between full-time and part-time employment, has also been scrutinized for its differential impact on the economic outlook.
    In addition, demographic shifts within the labor force and resulting consumption patterns are examined to pinpoint sectors like healthcare, technology, and financial services that may witness increased demand. Overlaying labor data with sector performance and earnings reports allows for a forward-looking approach to forecast which areas may experience earnings growth.
    As we finalize our analysis, robustness checks against various economic scenarios confirm that the bullish outlook is well-founded and not overly dependent on a single indicator. We, therefore, advise a diversified investment strategy that captures the potential for growth while providing a hedge against market volatility.

    Steady Trade Balance: A Signal of Market Stability for U.S. Equities\n
    According to our latest machine learning model analysis, the U.S. market is expected to maintain a stable outlook in the short term, supported by the steadiness in the Trade Balance data for goods and services on a quarter-over-quarter basis. The consistent SHAP value of 0.0084, despite a slight decrease in rank, points to an equilibrium in international trade flows, a key factor in the health of the U.S. economy and its equity markets.
    A balanced trade scenario is crucial for companies operating on a global scale, particularly in industries such as industrial goods and consumer products. The lack of significant change suggests a continuation of the status quo in international trade relations, which can be a boon for multinationals and export-driven sectors. For investors, the current trade data may offer reassurance that companies with significant exposure to international markets could see sustained operations without the risk of new trade barriers or fiscal imbalances.
    Our quantitative analysis extends to evaluating the correlation between trade balance figures and the performance of sectors closely tied to international trade, such as industrials and materials. This analysis aims to ascertain whether the observed trade balance stability translates into predictable sectoral growth and can be utilized to inform targeted investment strategies.
    Considering the wider implications, a stable trade balance may also mitigate currency exchange rate volatility, contributing to more stable and predictable earnings for internationally exposed firms. This effect is particularly pertinent for businesses within the technology and consumer goods sectors that benefit from a globalized supply chain.
    Incorporating additional macroeconomic variables like GDP growth rates and currency valuations enhances our model's predictive accuracy, providing investors with a more nuanced understanding of the trade balance's impact across various market segments. The analysis acknowledges the interconnected nature of global markets, where the stability of the U.S. trade balance can have ripple effects on international economic partners and, by extension, on U.S. equity markets.
    Our comprehensive report suggests a cautiously optimistic stance towards U.S. equities, highlighting opportunities in sectors poised to benefit from stable trade conditions. Investors are advised to maintain diversified portfolios to capitalize on these trends while safeguarding against potential disruptions in the global economic landscape.
    In conclusion, our multi-faceted approach confirms the positive alignment of current trade balance figures with a stable market outlook. The insights provided herein underscore the importance of strategic asset allocation in response to macroeconomic stability, emphasizing vigilance as investors navigate through a complex, interconnected economic environment.

    Labor Market Stability and its Market Implications\n
    The current assessment of the labor market reveals a stable outlook, as reflected by the consistent year-over-year SHAP value for civilian labor force volume over the last month. The stability, indicated by the SHAP value of 0.0076, is particularly noteworthy even as the metric experienced a marginal shift in its ranking. This constancy suggests an equilibrium in the labor market, a foundational element for sustained economic growth and a positive indicator for the stock market.
    The implications of a steady labor force resonate through various sectors of the economy, impacting consumer behavior and corporate performance. Stability in employment typically heralds continued consumer spending, a vital driver for sectors such as consumer discretionary and services. These sectors stand to benefit from the maintained purchasing power and confidence of a gainfully employed population.
    Our analysis extends to the intersection of labor data with equity market performance, examining past and present trends to forecast potential impacts. We have found that labor market stability often precedes steady demand in sectors tied closely to domestic economic conditions, offering predictive insights for strategic investment.
    Moreover, the interplay between wage levels and productivity is a critical factor to consider. Stable employment, coupled with proportional wage growth, can provide a favorable environment for equities, as it suggests a balance between consumer earning power and inflationary pressures.
    We have incorporated a spectrum of economic indicators, such as consumer confidence and retail sales, to provide a holistic view of how employment conditions affect the broader economy and, by extension, equity markets. These factors are particularly pertinent in shaping demand patterns and can significantly influence sector-specific performance.
    Demographic trends, including an aging workforce and evolving work patterns, have been analyzed for their long-term effects on market sectors. For example, increased healthcare demand due to an older population or technology adoption spurred by shifts in work patterns can offer investment opportunities.
    In the context of fiscal and monetary policy, labor market trends can inform sector resilience or vulnerability. Our analysis recommends a re-evaluation of sector allocations, favoring industries likely to sustain or improve performance in light of the current labor trends.
    Conclusively, the data underscores the importance of a diversified investment strategy. While the labor force's stability bodes well for a steady market outlook, investors are advised to remain vigilant and adaptive to economic changes that may influence market dynamics. The overall investment thesis advocates for a balanced approach, capitalizing on current market conditions while mitigating potential risks."""

    return stuff_to_show
def load_feature_data():
    import pandas as pd
    from io import StringIO

    # The provided string representation of the DataFrame
    top_features_20231030_str = '''                                                                                       Unnamed: 0  mean_shap       Type
    0       Employment, Employment, Payroll jobs, % month on month, Standardized, Chg P/P, Volume L0M   0.038708       ECON
    1                                                              Treasury Interest rate spreads L6M   0.012063       ECON
    2                                                            Personal Consumption Expenditure L1M   0.009410       ECON
    3                       Activity, Labour Force, Civilian labor force, total, Volume L1M (YOY-PCT)   0.009323       ECON
    4                                 Trade Balance, Total, Goods and services monthly data L0M (QOQ)   0.008407       ECON
    5                           Activity, Labour Force, Civilian labor force, total, Volume L1M (YOY)   0.007578       ECON
    6                                 Trade Balance, Total, Goods and services monthly data L4M (YOY)   0.006518       ECON
    7                                                        Reserve Assets, Current Prices L1M (QOQ)   0.006470       ECON
    8                                 Trade Balance, Total, Goods and services monthly data L6M (YOY)   0.006377       ECON
    9                                                          Leading Index, Total, SA L1M (MOM-PCT)   0.006375       ECON
    10                            Trade Balance, Total, Goods and services monthly data L4M (YOY-PCT)   0.005772       ECON
    11                                                 Federal budget you need to normalize L3M (MOM)   0.005652       ECON
    12                            Trade Balance, Total, Goods and services monthly data L6M (YOY-PCT)   0.004515       ECON
    13                                                         Money supply M1, SA, USD L6M (YOY-PCT)   0.004400       ECON
    14                                                   Reserve Assets, Current Prices L2M (QOQ-PCT)   0.004198       ECON
    15                                                             Money supply M1, SA, USD L5M (YOY)   0.004149       ECON
    16                          CPI - All Urban Sample: All Items - Annual Inflation Rate, Not SA L6M   0.003554       ECON
    17                                                         Money supply M1, SA, USD L5M (YOY-PCT)   0.003173       ECON
    18                                          Wholesale Inventories/Sales Ratio, Current Prices L3M   0.003172       ECON
    19                                                             Treasury Interest rate spreads L1M   0.003145       ECON
    20                                                             Leading Index, Total, SA L1M (MOM)   0.003130       ECON
    21        Employment, Employment, Payroll jobs, % year on year, Standardized, Chg Y/Y, Volume L4M   0.003088       ECON
    22                                                             Money supply M1, SA, USD L0M (MOM)   0.003015       ECON
    23                                                             Money supply M2, SA, USD L2M (YOY)   0.003009       ECON
    24                                                             Money supply M2, SA, USD L4M (QOQ)   0.002911       ECON
    25  Employment, By Industry, Nonfarm payroll, goods-producing, manufacturing, total, SA L3M (YOY)   0.002838       ECON
    26                                                   Reserve Assets, Current Prices L0M (QOQ-PCT)   0.002760       ECON
    27                            Imports, Goods and services, Current Prices, adjusted L0M (QOQ-PCT)   0.002704  TECHNICAL
    28                                                    Total credit (monthly change) L6M (QOQ-PCT)   0.002671  TECHNICAL
    29                            Trade Balance, Total, Goods and services monthly data L5M (YOY-PCT)   0.002643  TECHNICAL'''

    # The provided string representation of the DataFrame
    top_features_20230928_str = '''                                                                                       Unnamed: 0  mean_shap       Type
    0       Employment, Employment, Payroll jobs, % month on month, Standardized, Chg P/P, Volume L0M   0.031133       ECON
    1                                                              Treasury Interest rate spreads L6M   0.013574       ECON
    2                       Activity, Labour Force, Civilian labor force, total, Volume L1M (YOY-PCT)   0.008551       ECON
    3                                 Trade Balance, Total, Goods and services monthly data L0M (QOQ)   0.008407       ECON
    4                           Activity, Labour Force, Civilian labor force, total, Volume L1M (YOY)   0.007578       ECON
    5                                 Trade Balance, Total, Goods and services monthly data L4M (YOY)   0.006518       ECON
    6                                                        Reserve Assets, Current Prices L1M (QOQ)   0.006470       ECON
    7                                 Trade Balance, Total, Goods and services monthly data L6M (YOY)   0.006377       ECON
    8                                                          Leading Index, Total, SA L1M (MOM-PCT)   0.006375       ECON
    9                             Trade Balance, Total, Goods and services monthly data L4M (YOY-PCT)   0.005772       ECON
    10                            Trade Balance, Total, Goods and services monthly data L6M (YOY-PCT)   0.004515       ECON
    11                                                         Money supply M1, SA, USD L6M (YOY-PCT)   0.004400       ECON
    12                                                   Reserve Assets, Current Prices L2M (QOQ-PCT)   0.004198       ECON
    13                                                             Money supply M1, SA, USD L5M (YOY)   0.004149       ECON
    14                                                 Federal budget you need to normalize L3M (MOM)   0.003739       ECON
    15                          CPI - All Urban Sample: All Items - Annual Inflation Rate, Not SA L6M   0.003554       ECON
    16                                                           Personal Consumption Expenditure L1M   0.003543       ECON
    17                                                         Money supply M1, SA, USD L5M (YOY-PCT)   0.003173       ECON
    18                                          Wholesale Inventories/Sales Ratio, Current Prices L3M   0.003172       ECON
    19                                                             Treasury Interest rate spreads L1M   0.003145       ECON
    20        Employment, Employment, Payroll jobs, % year on year, Standardized, Chg Y/Y, Volume L4M   0.003141       ECON
    21                                                             Leading Index, Total, SA L1M (MOM)   0.003130       ECON
    22                                                             Money supply M1, SA, USD L0M (MOM)   0.003015       ECON
    23                                                             Money supply M2, SA, USD L2M (YOY)   0.003009       ECON
    24                                                             Money supply M2, SA, USD L4M (QOQ)   0.002911       ECON
    25  Employment, By Industry, Nonfarm payroll, goods-producing, manufacturing, total, SA L3M (YOY)   0.002838       ECON
    26                                                   Reserve Assets, Current Prices L0M (QOQ-PCT)   0.002760       ECON
    27                            Imports, Goods and services, Current Prices, adjusted L0M (QOQ-PCT)   0.002704  TECHNICAL
    28                                                    Total credit (monthly change) L6M (QOQ-PCT)   0.002671  TECHNICAL
    29                            Trade Balance, Total, Goods and services monthly data L5M (YOY-PCT)   0.002643  TECHNICAL'''

    # Convert the string into a file-like object
    #string_io = StringIO(top_features_20230928_str)

    # Read the string into a DataFrame
    # Using '\s{2,}' as the delimiter to match two or more whitespace characters
    previous_top_features_df = pd.read_csv(StringIO(top_features_20230928_str), sep='\s{2,}', engine='python')

    # Read the string into a DataFrame
    # Using '\s{2,}' as the delimiter to match two or more whitespace characters
    today_top_features_df = pd.read_csv(StringIO(top_features_20231030_str), sep='\s{2,}', engine='python')

    today_top_features_df.index.name = 'Rank'
    today_top_features_df.columns = ['Feature', 'Shap', 'Type']
    previous_top_features_df.index.name = 'Rank'
    previous_top_features_df.columns = ['Feature', 'Shap', 'Type']
    return today_top_features_df, previous_top_features_df

def create_gauge_plot(state, previous_state):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=state,
        domain={'x': [0, 1], 'y': [0, 1]},
       #title={'text': "Market State"},
        delta={'reference': previous_state, 'relative': False, 'increasing': {'color': "RebeccaPurple"},
               'decreasing': {'color': "RoyalBlue"}},

        gauge={
            'axis': {'range': [None, 2], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            #'bgcolor': "white",
            'borderwidth': 0,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 0.75], 'color': 'darkgreen'},
                {'range': [0.75,1.25], 'color': 'yellow'},
                {'range': [1.25, 2], 'color': 'darkred'}
            ],
            'threshold': {
                'line': {'color': "blue", 'width': 4},

                'thickness': 0.75,
                'value': state
            }
        }
    ))

    font_size  = 24
    # Adding annotations for labels
    fig.update_layout(
        annotations=[
            go.layout.Annotation(x=1.-0.1, y=-0.25, text="Bearish", font={"size":font_size}, showarrow=False),
            go.layout.Annotation(x=0.+0.1, y=-0.25, text="Bullish", font={"size":font_size},showarrow=False),
            go.layout.Annotation(x=0.5, y=0.75, text="Calm", font={"size":font_size}, showarrow=False)
        ]
    )

    #number={'prefix': 'BTC'}
    #height = 50,  # Adjust the height of the gauge plot
    #width = 400  # Adjust the width of the gauge plot
    return fig


############## define demo data ##############
current_state = 1
previous_state = 2
n_days_prediction_df = (
    pd.DataFrame(data={
    '1D': [0],
    '3D': [1],
    '5D': [0],
    '10D': [2],
    '15D': [2],
},index=['Market State']))


#from signal_rnd.gen2_macro_signals.thomas_xgboost.AGI.df_2_string import load_feature_data
today_top_features_df, previous_top_features_df = load_feature_data()
st.set_page_config(page_title='AGI Market Analytics by MechaniX Ltd.', page_icon='📊', layout='wide')


def diff_dataframes_rank(current_df_, previous_df):
    # Ensure that the 'Feature' column is the same in both DataFrames for a valid comparison
    #if not current_df['Feature'].equals(previous_df['Feature']):
    #    raise ValueError("The Feature columns in both DataFrames must be identical.")

    # Assign ranks to the rows in both DataFrames
    current_df = current_df_.copy()
    current_df['Rank_Current'] = current_df.index + 1
    previous_df['Rank_Previous'] = previous_df.index + 1

    # Merge the two DataFrames based on 'Feature' column to align the rows
    merged_df = pd.merge(current_df, previous_df, on='Feature')

    # Calculate the difference in ranks
    merged_df['Rank_Difference'] = merged_df['Rank_Current'] - merged_df['Rank_Previous']

    # Create the resulting DataFrame with required columns
    result_df = pd.DataFrame({
        'Feature': merged_df['Feature'],
        'Type': merged_df['Type_x'],  # Assuming 'Type' doesn't change between DataFrames
        'Rank_Difference': merged_df['Rank_Difference']
    })

    # Sort by 'Rank_Difference' in descending order
    result_df.sort_values(by='Rank_Difference', ascending=False, inplace=True)

    return result_df


def make_feature_leader_board(today_top_features_df, previous_top_features_df):

    ascending_df = diff_dataframes_rank(current_df_ = today_top_features_df, previous_df = previous_top_features_df)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Today's top 10 features")
        st.dataframe(today_top_features_df[0:11], use_container_width=True)
    with col2:
        st.subheader("Top ascend features")
        st.dataframe(ascending_df[0:11][['Feature','Type']], use_container_width=True,hide_index=True)
    with col3:
        st.subheader("Top decline features")
        declining_df = ascending_df.sort_values(by='Rank_Difference', ascending=True)
        st.dataframe(declining_df[0:11][['Feature','Type']], use_container_width=True,hide_index=True)
############## end demo data ##############

#st.set_page_config(page_title="LangChain: Chat with search", page_icon="🦜")
#st.title("🦜 AGI Market Analytics")
st.title("AGI Market Analytics")

#openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


fig_placeholder = st.container()

gauge_plot = create_gauge_plot(current_state, previous_state=previous_state)
with fig_placeholder:
    st.plotly_chart(gauge_plot, theme='streamlit', use_container_width=True)

st.write('Data as of 2022-10-30 00:00:00 EST, target index S&P500.')
st.divider()

# N day ahead forecast
st.subheader("Market state forecast")

# Display the DataFrame using AgGrid
# AgGrid configuration
grid_options = {
    #'height': '75px',  # Adjust the height as needed
    'fit_columns_on_grid_load': False
}

grid_response = st.table(n_days_prediction_df)#, grid_options)

st.write(""" Summary: \n
The market is predicted to maintain stability on day 1, followed by a surge of bullish activity on day 3. By day 5, the market stabilizes again, possibly as it adjusts to the recent activity. Looking ahead to days 10 and 15, a bearish trend is anticipated, suggesting that investors may need to exercise caution. Strategies could include taking advantage of the bullish period for short-term trades while preparing for a potential downturn by reinforcing defensive measures as the forecast matures.""")

st.divider()

##################################################################################
st.title("🦜 Generative report")

# this is the main dodge
st.divider()
# N day ahead forecast
st.subheader("Generative report")
# Sample data for the dropdown list
options = ["top 3", "top 5", "top 10", "econ focus", "top 10 technical"]

# Creating a dropdown list
selected_option = st.selectbox("Choose an option:", options)
# Displaying the selected option
st.write("You selected:", selected_option)

stuff_to_show = load_demo_article()
st.download_button(label="Download report", data=stuff_to_show, file_name="report.txt", mime="text/plain")

if selected_option == "top 3":
    st.dataframe(today_top_features_df[0:3], use_container_width=True)

if selected_option == "top 5":
    st.dataframe(today_top_features_df[0:5], use_container_width=True)
    st.write(stuff_to_show)

if selected_option == "top 10":
    st.dataframe(today_top_features_df[0:10], use_container_width=True)
    st.write(stuff_to_show)

st.divider()
make_feature_leader_board(today_top_features_df, previous_top_features_df)



# #openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

# msgs = StreamlitChatMessageHistory()
# memory = ConversationBufferMemory(
#     chat_memory=msgs, return_messages=True, memory_key="chat_history", output_key="output"
# )
# if len(msgs.messages) == 0 or st.sidebar.button("Reset chat history"):
#     msgs.clear()
#     msgs.add_ai_message("How can I help you?")
#     st.session_state.steps = {}
#
# avatars = {"human": "user", "ai": "assistant"}
# for idx, msg in enumerate(msgs.messages):
#     with st.chat_message(avatars[msg.type]):
#         # Render intermediate steps if any were saved
#         for step in st.session_state.steps.get(str(idx), []):
#             if step[0].tool == "_Exception":
#                 continue
#             with st.status(f"**{step[0].tool}**: {step[0].tool_input}", state="complete"):
#                 st.write(step[0].log)
#                 st.write(step[1])
#         st.write(msg.content)
#
# if prompt := st.chat_input(placeholder="Who won the Women's U.S. Open in 2018?"):
#     st.chat_message("user").write(prompt)
#
#     if not openai_api_key:
#         st.info("Please add your OpenAI API key to continue.")
#         st.stop()
#
#     llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True)
#     tools = [DuckDuckGoSearchRun(name="Search")]
#     chat_agent = ConversationalChatAgent.from_llm_and_tools(llm=llm, tools=tools)
#     executor = AgentExecutor.from_agent_and_tools(
#         agent=chat_agent,
#         tools=tools,
#         memory=memory,
#         return_intermediate_steps=True,
#         handle_parsing_errors=True,
#     )
#     with st.chat_message("assistant"):
#         st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
#         response = executor(prompt, callbacks=[st_cb])
#         st.write(response["output"])
#         st.session_state.steps[str(len(msgs.messages) - 1)] = response["intermediate_steps"]
