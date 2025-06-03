import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Produk", layout="wide")
st.title("📊 Dashboard Analisis Kinerja Penjualan")

df = pd.read_csv('https://raw.githubusercontent.com/AleisyaZahari/Project-Data-Analytics-with-Streamlit/main/dashboard/all_data.csv') # ← ini yang benar

# Sidebar filter (opsional)
with st.sidebar:
    st.header("🔍 Filter")
    tahun_opsi = ['Semua Tahun'] + sorted(df['order_purchase_timestamp'].str[:4].unique().tolist())
    tahun_terpilih = st.selectbox("Pilih Tahun", tahun_opsi)
    # st.markdown("### ℹ️ Informasi")
    # st.markdown("**Nama:** Aleisya Zahari Salam")
    # st.markdown("**Proyek:** Submission Akhir Dicoding")
    # st.markdown("**Tujuan:** Analisis performa penjualan berdasarkan kategori, waktu, dan metode pembayaran.")
    # st.markdown("⬇ Gunakan filter tahun di bawah ini:")

if tahun_terpilih != 'Semua Tahun':
    df = df[df['order_purchase_timestamp'].str[:4] == tahun_terpilih]

st.subheader("📦 5 Produk Penjualan Terlaris dan Terendah")
product_id_counts = df.groupby('product_category_name_english')['product_id'].count().reset_index()
product_id_counts = product_id_counts.sort_values(by='product_id', ascending=False)
product_id_counts = product_id_counts.rename(columns={'product_id': 'Product Count', 'product_category_name_english': 'Product Category'})
# product_id_counts
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(27, 6))

# --- Data ---
top_5 = product_id_counts.head(5)
least_5 = product_id_counts.sort_values(by="Product Count", ascending=True).head(5)

# --- Barplot kiri (terbanyak) ---
bars1 = sns.barplot(
    x="Product Count", y="Product Category",
    data=top_5,
    ax=ax[0]
)
for i, bar in enumerate(bars1.patches):
    color = "#72BCD4" if i == 0 else "#D3D3D3"
    bar.set_color(color)

    # Tambahkan label di ujung bar
    ax[0].text(
        bar.get_width() + 0.5,  # geser sedikit kanan
        bar.get_y() + bar.get_height()/2,
        f'{bar.get_width():,.0f}',
        va='center', fontsize=11
    )

ax[0].set_xlabel("Jumlah Produk", fontsize=12)
ax[0].set_ylabel(None)
ax[0].set_title("Produk dengan Penjualan Terbanyak", fontsize=16)
ax[0].tick_params(axis='y', labelsize=12)

# --- Barplot kanan (terendah) ---
bars2 = sns.barplot(
    x="Product Count", y="Product Category",
    data=least_5,
    ax=ax[1]
)
for i, bar in enumerate(bars2.patches):
    color = "#72BCD4" if i == 0 else "#D3D3D3"
    bar.set_color(color)

    # Tambahkan label di ujung bar
    ax[1].text(
        bar.get_width() + 0.5,
        bar.get_y() + bar.get_height()/2,
        f'{bar.get_width():,.0f}',
        va='center', fontsize=11
    )


ax[1].set_xlabel("Jumlah Produk", fontsize=12)
ax[1].set_ylabel(None)
ax[1].set_title("Produk dengan Penjualan Terendah", fontsize=16)
ax[1].tick_params(axis='y', labelsize=12)
ax[0].spines['right'].set_visible(False)
ax[0].spines['top'].set_visible(False)

ax[1].spines['right'].set_visible(False)
ax[1].spines['top'].set_visible(False)

# --- Layout ---
plt.suptitle("Kategori Produk Penjualan Terlaris dan Terendah", fontsize=20)
plt.tight_layout(rect=[0, 0, 1, 0.95])

st.pyplot(fig)

# with st.expander("Penjelasan"):
#     st.write(
#         """
#  - Kategori Produk Terlaris:

#     - Bed, Bath & Table dengan 11.988 unit terjual, menduduki peringkat pertama sebagai produk yang paling banyak terjual.

#     - Health & Beauty dan Sports & Leisure juga menunjukkan angka penjualan yang tinggi dengan masing-masing 10.032 dan 9.004 unit terjual.

#   - Kategori Produk Tersedikit:

#     - Security and Services adalah kategori dengan penjualan terendah, hanya 2 unit terjual.

#     - Arts and Craftsmanship juga sangat rendah, hanya mencatatkan 24 unit terjual, diikuti dengan kategori Fashion Children's Clothes yang terjual 8 unit.

#   **Kesimpulan**: Produk dengan kategori yang lebih umum dan fungsional, seperti bed_bath_table dan health_beauty, menunjukkan performa penjualan yang lebih tinggi, sementara kategori yang lebih spesifik atau lebih niche, seperti arts_and_craftsmanship dan security_and_services, menunjukkan penjualan yang sangat rendah.
#         """
#     )
with st.expander("Penjelasan"):
    st.write("### 📈 Ringkasan Penjualan")
    st.markdown("### 🔹5 Produk Terlaris:")
    st.markdown(
        f"  - Produk **{top_5.iloc[0]['Product Category']}** terjual sebanyak **{top_5.iloc[0]['Product Count']}** unit, menduduki peringkat pertama sebagai produk yang paling banyak terjual."
    )
    st.markdown(
        f"  - Diikuti oleh **{top_5.iloc[1]['Product Category']}** dengan **{top_5.iloc[1]['Product Count']}** unit, dan **{top_5.iloc[2]['Product Category']}** dengan **{top_5.iloc[2]['Product Count']}** unit."
    )

    st.markdown("### 🔸5 Produk dengan Penjualan Terendah:")
    st.markdown(
        f"  - Produk **{least_5.iloc[0]['Product Category']}** adalah yang paling sedikit terjual, hanya **{least_5.iloc[0]['Product Count']}** unit."
    )
    st.markdown(
        f"  - Diikuti oleh **{least_5.iloc[1]['Product Category']}** dengan **{least_5.iloc[1]['Product Count']}** unit, dan **{least_5.iloc[2]['Product Category']}** dengan **{least_5.iloc[2]['Product Count']}** unit."
    )

    # st.markdown(
    #     "**Kesimpulan**: Produk-produk dengan kebutuhan fungsional umum cenderung lebih laris, sementara kategori yang spesifik atau niche memiliki angka penjualan yang jauh lebih rendah."
    # )

#     st.markdown("""
# **Kesimpulan**: Kategori produk yang bersifat umum dan kebutuhan rumah tangga cenderung mencatat penjualan lebih tinggi, sementara kategori spesifik atau niche memiliki volume penjualan lebih rendah.  
# Gunakan insight ini untuk pertimbangan strategi stok atau promosi.
# """)

st.subheader("📈 Jumlah Order per Bulan")
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'], errors='coerce')

df['order_month'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)

monthly_orders = df.groupby('order_month').size().reset_index(name='total_orders')

# Pastikan format string untuk sumbu x
monthly_orders['order_month'] = monthly_orders['order_month'].astype(str)

# Cari posisi index tiap awal tahun
monthly_orders = monthly_orders.sort_values('order_month')
tick_positions = monthly_orders.reset_index().reset_index()  # dua reset_index buat ngambil posisi integer
year_start_positions = (
    tick_positions
    .groupby(monthly_orders['order_month'].str[:4])
    .first()['level_0']
    .values[1:]  # skip tahun pertama, karena pembatas mulai dari tahun berikutnya
)

# --- Visualisasi ---
plt.figure(figsize=(14, 6))
sns.lineplot(data=monthly_orders, x='order_month', y='total_orders', marker='o', color='#72BCD4')

# Tambahkan label di atas titik
for x, y in zip(monthly_orders['order_month'], monthly_orders['total_orders']):
    plt.text(
        x,
        y + (monthly_orders['total_orders'].max() * 0.01),
        str(y),
        ha='center',
        va='bottom',
        fontsize=8
    )

# Tambahkan garis vertikal pemisah antar tahun
for xpos in year_start_positions:
    plt.axvline(x=xpos - 0.5, color='#999999', linestyle='--', alpha=0.7)

plt.xticks(rotation=45)
plt.title('Jumlah Order per Bulan', fontsize=14)
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Jumlah Order', fontsize=12)
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

st.pyplot(plt.gcf())  # gcf = get current figure
bulan_terbanyak = monthly_orders.loc[monthly_orders['total_orders'].idxmax()]
bulan_tersedikit = monthly_orders.loc[monthly_orders['total_orders'].idxmin()]

# with st.expander("Penjelasan"):
#     st.write("""
#     Dari data pembelian setiap bulan, terlihat adanya fluktuasi yang signifikan dalam jumlah order:

#   - Puncak Pembelian: Pembelian tertinggi tercatat pada bulan November 2017, dengan 9.096 order. Puncak ini menunjukkan periode tinggi untuk pembelian, mungkin karena promosi atau event khusus pada bulan tersebut.

#   - Penurunan Pembelian: Pembelian terendah tercatat pada September 2016 dengan hanya 6 order, yang menunjukkan bahwa data dimulai pada periode rendah dan kemudian meningkat drastis seiring waktu.

#   **Kesimpulan**: Ada tren kenaikan volume pembelian yang signifikan mulai 2017 hingga 2018, dengan puncak tertinggi pada akhir 2017, yang bisa menunjukkan pengaruh dari kampanye musiman atau acara tertentu.

#     """)
with st.expander("Penjelasan"):
    st.markdown("### 📊 Analisis Tren Order Bulanan:")
    st.markdown(
        f"- **Puncak Pembelian:** terjadi pada **{bulan_terbanyak['order_month']}** "
        f"dengan **{bulan_terbanyak['total_orders']:,}** order, kemungkinan dipengaruhi oleh kampanye promosi atau momen belanja tertentu."
    )
    st.markdown(
        f"- **Jumlah Order Terendah:** tercatat pada **{bulan_tersedikit['order_month']}** "
        f"dengan hanya **{bulan_tersedikit['total_orders']:,}** order, yang bisa menandakan awal data atau periode sepi transaksi."
    )
    # st.markdown(
    #     "**Kesimpulan:** Secara umum, jumlah order menunjukkan tren naik dari waktu ke waktu, "
    #     "dengan fluktuasi yang bisa dipengaruhi oleh musim belanja, promosi, atau faktor eksternal lainnya."
    # )

st.subheader("💳 Metode Pembayaran Terpopuler")

# payment_counts = (
#     df.groupby("payment_type")
#     .size()
#     .reset_index(name="count")
#     .sort_values("count", ascending=False)
# )

# fig, ax = plt.subplots(figsize=(10, 5))
# sns.barplot(x='count', y='payment_type', data=payment_counts, palette='coolwarm', ax=ax)
# ax.set_title("Jumlah Transaksi per Metode Pembayaran")
payment_counts = (
    df.groupby("payment_type")
    .size()
    .reset_index(name="count")
    .sort_values("count", ascending=False)
)

# Buat figure dan axis
fig, ax = plt.subplots(figsize=(10, 5))

# Buat barplot
sns.barplot(data=payment_counts, x="count", y="payment_type", ax=ax)

# Pewarnaan bar dan label
for i, bar in enumerate(ax.patches):
    bar.set_color("#72BCD4" if i == 0 else "#D3D3D3")
    ax.text(
        bar.get_width() + 0.5,
        bar.get_y() + bar.get_height() / 2,
        f'{bar.get_width():,.0f}',
        va='center', fontsize=11
    )

# Hiasan visual
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_title("Metode Pembayaran Terpopuler")
ax.set_xlabel("Jumlah Transaksi")
ax.set_ylabel(None)
plt.tight_layout()
st.pyplot(plt.gcf())
# with st.expander("Penjelasan"):
#     st.write("""
#     Metode pembayaran yang paling banyak digunakan adalah:

#   - Credit Card yang digunakan oleh 87.258 pelanggan, mendominasi sebagai metode pembayaran utama.

#   - Boleto menjadi pilihan kedua dengan 23.018 transaksi.

#   - Voucher dan Debit Card tercatat dengan jumlah masing-masing 6.332 dan 1.699.

#   **Kesimpulan**: Credit card adalah metode pembayaran yang paling disukai oleh pelanggan, dengan Boleto menjadi alternatif yang cukup populer di pasar. Debit card dan voucher memiliki angka transaksi yang jauh lebih rendah, yang menunjukkan bahwa mereka mungkin lebih jarang digunakan atau dipilih berdasarkan kebutuhan spesifik.

#     """)
top_payments = payment_counts.head(4).reset_index(drop=True)
with st.expander("Penjelasan"):
    st.markdown("### 💬 Analisis Metode Pembayaran Terpopuler:")

    # Loop setiap metode pembayaran terpopuler
    urutan = ["pertama", "kedua", "ketiga", "keempat"]
    f"""- 
    Metode pembayaran yang paling banyak digunakan adalah **{top_payments.loc[0, 'payment_type'].title()}**, dengan jumlah transaksi mencapai **{top_payments.loc[0, 'count']:,}**"""
    f"""- Di posisi berikutnya, metode seperti **{top_payments.loc[1, 'payment_type'].title()}** dan **{top_payments.loc[2, 'payment_type'].title()}** juga menunjukkan popularitas yang cukup tinggi, meskipun angkanya jauh di bawah metode utama.
"""
# **Kesimpulan:** Terlihat bahwa pelanggan cenderung memilih metode pembayaran yang praktis, dengan satu metode mendominasi lebih dari setengah total transaksi.
# """
#     for i, row in top_payments.iterrows():
        
#         st.markdown(
#             f"- **{row['payment_type'].title()}** digunakan sebanyak **{row['count']:,}** kali, "
#             f"menduduki peringkat {urutan[i]} sebagai metode pembayaran yang paling sering digunakan."
#         )

#     st.markdown(
#     f"**Kesimpulan:** Metode pembayaran dengan **{top_payments.loc[0, 'payment_type'].title()}** mendominasi transaksi, "
#     f"diikuti oleh metode lain seperti **{top_payments.loc[1, 'payment_type'].title()}**, "
#     f"**{top_payments.loc[2, 'payment_type'].title()}**, dan **{top_payments.loc[3, 'payment_type'].title()}**. "
    # )

st.subheader("🧮 RFM Analysis - Top 5 Customers")

# now = df['order_purchase_timestamp'].max()
# rfm_df = df.copy()

# recency = (now - rfm_df.groupby('customer_id')['order_purchase_timestamp'].max()).dt.days
# frequency = rfm_df.groupby('customer_id')['order_id'].nunique()
# monetary = rfm_df.groupby('customer_id')['price'].sum()

# rfm = pd.DataFrame({
#     'customer_id': recency.index,
#     'Recency': recency.values,
#     'Frequency': frequency.values,
#     'Monetary': monetary.values
# })
# rfm['short_id'] = rfm['customer_id'].str[:8]

# fig, ax = plt.subplots(1, 3, figsize=(20, 6))

# sns.barplot(data=rfm.sort_values(by='Recency').head(5), x='short_id', y='Recency', ax=ax[0])
# ax[0].set_title('Top Recency')

# sns.barplot(data=rfm.sort_values(by='Frequency', ascending=False).head(5), x='short_id', y='Frequency', ax=ax[1])
# ax[1].set_title('Top Frequency')

# sns.barplot(data=rfm.sort_values(by='Monetary', ascending=False).head(5), x='short_id', y='Monetary', ax=ax[2])
# ax[2].set_title('Top Monetary')
df['order_purchase_timestamp'].max()

now = df['order_purchase_timestamp'].max()

# Hitung RFM
recency = (now - df.groupby('customer_id')['order_purchase_timestamp'].max()).dt.days
frequency = df.groupby('customer_id')['order_id'].count()
monetary = df.groupby('customer_id')['price'].sum()

# Gabungkan jadi DataFrame
rfm = pd.DataFrame({
    'customer_id': recency.index,
    'Recency': recency.values,
    'Frequency': frequency.values,
    'Monetary': monetary.values
})
rfm.sort_values(by='Recency',ascending=True)
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 10))
rfm['short_id'] = rfm['customer_id'].str[:8]  # hanya 8 karakter pertama

# RECENCY
top_recency = rfm.sort_values(by="Recency", ascending=True).head(5)
sns.barplot(palette=['#72BCD4'], y="Recency", x="short_id", data=top_recency, ax=ax[0])
ax[0].set_title("By Recency (days)", fontsize=18)
ax[0].set_xlabel("Customer ID", fontsize=14)
ax[0].set_ylabel(None)
ax[0].tick_params(axis='x', rotation=90)

for p in ax[0].patches:
    ax[0].annotate(f"{int(p.get_height())}", 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha='center', va='bottom', fontsize=12, color='black')

# FREQUENCY
top_frequency = rfm.sort_values(by="Frequency", ascending=False).head(5)
sns.barplot(palette=['#72BCD4'], y="Frequency", x="short_id", data=top_frequency, ax=ax[1])
ax[1].set_title("By Frequency", fontsize=18)
ax[1].set_xlabel("Customer ID", fontsize=14)
ax[1].set_ylabel(None)
ax[1].tick_params(axis='x', rotation=90)

for p in ax[1].patches:
    ax[1].annotate(f"{int(p.get_height())}", 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha='center', va='bottom', fontsize=12, color='black')

# MONETARY
top_monetary = rfm.sort_values(by="Monetary", ascending=False).head(5)
sns.barplot(palette=['#72BCD4'], y="Monetary", x="short_id", data=top_monetary, ax=ax[2])
ax[2].set_title("By Monetary", fontsize=18)
ax[2].set_xlabel("Customer ID", fontsize=14)
ax[2].set_ylabel(None)
ax[2].tick_params(axis='x', rotation=90)

for p in ax[2].patches:
    ax[2].annotate(f"{p.get_height():.2f}", 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha='center', va='bottom', fontsize=12, color='black')

# Judul utama
plt.suptitle("Top 5 Kostumer berdasarkan metriks RFM", fontsize=22)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
st.pyplot(fig)

with st.expander("Penjelasan"):
    st.write("""

 1. Recency (Semakin kecil, semakin baru)
    - Pelanggan ini masih recently active.
    - Mereka bisa jadi target utama untuk email marketing, upsell, atau promo lanjutan karena mereka masih hangat.

2. Frequency (Jumlah order terbanyak)
    - Mereka loyal dan menunjukkan repeat behavior.
    - Bisa jadikan target loyalty program, subscription offer, atau bahkan brand ambassador.

3. Monetary (Total nilai pembelian tertinggi)
    - Mereka adalah high-value customers.
    - Prioritaskan mereka dalam personalized offers atau premium service.
    """)
st.markdown("---")
st.markdown("### ℹ️ Tentang Proyek")
st.markdown("""
- **Nama:** Aleisya Zahari Salam  
- **Proyek:** Submission Akhir Dicoding - Belajar Analisis Data dengan Python  
- **Tujuan:** Menganalisis performa penjualan berdasarkan kategori produk, waktu, dan metode pembayaran.  
- Gunakan sidebar di kiri untuk memfilter data berdasarkan tahun.
""")
