from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, BigInteger, Index
from sqlalchemy.orm import relationship
from app.db import Base
import datetime

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String(16), unique=True, index=True, nullable=False)  # e.g., AAPL, MSFT
    name = Column(String(256), nullable=True)

    # relación a precios; back_populates permite navegación bidireccional
    prices = relationship("StockPrice", back_populates="company", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Company {self.ticker} ({self.name})>"

class StockPrice(Base):
    __tablename__ = "stock_prices"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    timestamp = Column(DateTime, nullable=False, index=True)  # fecha/hora del precio
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(BigInteger, nullable=True)

    company = relationship("Company", back_populates="prices")

    # Índice útil para consultas por company + timestamp
    __table_args__ = (
        Index("ix_stock_company_ts", "company_id", "timestamp"),
    )

    def __repr__(self):
        return f"<Price {self.company_id} {self.timestamp} close={self.close}>"
