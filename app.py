import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
from io import BytesIO

# Function to scrape data from a website
def scrape_data(url, tag, class_name, value_type, attribute):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        if class_name.strip():
            elements = soup.find_all(tag, class_=class_name)
        else:
            elements = soup.find_all(tag)
        
        data = []
        image_urls = []
        
        if value_type == "Image" and attribute:
            for index, element in enumerate(elements):
                if element.has_attr(attribute):
                    img_url = element[attribute]
                    # Ensure absolute URL
                    if not img_url.startswith('http'):
                        img_url = url.rstrip('/') + '/' + img_url.lstrip('/')
                    title = element.get("alt", "No Title")
                    data.append({"Image URL": img_url, "Title": title})
                    image_urls.append((img_url, f"image_{index}.jpg"))
            return data, image_urls
        else:
            for element in elements:
                if value_type == "Text":
                    data.append({"Scraped Data": element.get_text(strip=True)})
                elif value_type == "Attribute" and attribute:
                    data.append({"Scraped Data": element.get(attribute, "N/A")})
            return data, None
    except Exception as e:
        st.error(f"Error scraping data: {e}")
        return None, None

# Streamlit UI
def main():
    # Custom UI
    st.title("🌐 Tamiko Web Scraper")
    st.markdown("**Scrape text, images, or attributes from any website with ease!**")
    st.markdown("---")
    
    # User Inputs with default placeholder
    url = st.text_input("Enter Website URL:", "")
    tag = st.text_input("Enter HTML Tag to Scrape:", "div")
    class_name = st.text_input("Enter Class Name (optional):", "")
    value_type = st.selectbox("Select Data Type:", ["Text", "Image", "Attribute"])
    attribute = st.text_input("Enter Attribute (e.g., 'src' for images, leave blank if not needed):", "")
    
    # Scrape button
    if st.button("Scrape Data", key="scrape_button"):
        if not url.strip():
            st.warning("Please enter a valid website URL.")
        else:
            with st.spinner("Scraping data... Please wait."):
                data, image_urls = scrape_data(url, tag, class_name, value_type, attribute)
                
                if data:
                    df = pd.DataFrame(data)
                    
                    # Display results
                    st.markdown("### Scraped Results")
                    st.dataframe(df, use_container_width=True)
                    
                    if value_type == "Image" and image_urls:
                        # Create individual image downloads
                        for img_url, filename in image_urls:
                            img_response = requests.get(img_url, stream=True)
                            if img_response.status_code == 200:
                                img_buffer = BytesIO(img_response.content)
                                st.download_button(
                                    label=f"Download {filename}",
                                    data=img_buffer,
                                    file_name=filename,
                                    mime="image/jpeg"
                                )
                        
                        # Save image URLs to Excel
                        excel_buffer = BytesIO()
                        df.to_excel(excel_buffer, index=False)
                        excel_buffer.seek(0)
                        st.success("Images scraped successfully!")
                        st.download_button(
                            label="Download Image URLs as Excel",
                            data=excel_buffer,
                            file_name="tamiko_scraped_images.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )
                    else:
                        # Save text/attribute data to Excel
                        excel_buffer = BytesIO()
                        df.to_excel(excel_buffer, index=False)
                        excel_buffer.seek(0)
                        st.success("Data scraped successfully!")
                        st.download_button(
                            label="Download Data as Excel",
                            data=excel_buffer,
                            file_name="tamiko_scraped_data.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )

if __name__ == "__main__":
    main()      